from django.shortcuts import render
from django.views.generic import View
from cricapp.models import *
import json
from cricapp.mixins import *
from cricapp.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from cricapp.utils import is_valid_json_data
from django.core.serializers import serialize
from django.http import HttpResponse

@method_decorator(csrf_exempt,name='dispatch')
class CricketerCRUDCbv(View,SerializeMixin,HttpMixinResponse):
    ''' This class extends the View and HttpMixinResponse '''
    def get_object_data_by_id(self,id):
        '''
        This function will fetch the record[data] present within DB using id
        '''
        try:
             cric = Cricketer.objects.get(id=id)
        except Cricketer.DoesNotExist:
            cric = None
        return cric

    def get(self,request,*args, **kwargs):
        ''' This function is used to fetch the data from Database(DB) '''
        data = request.body
        valid_jason_data = is_valid_json_data(data)
        if not valid_jason_data:
            json_data = json.dumps({'msg':'Please send the valid json data'})
            return self.render_to_http_response(json_data, status=400)

        provided_data = json.loads(data)
        id = provided_data.get('id',None)
        if id is not None:
            cric = self.get_object_data_by_id(id)
            if cric is None:
                json_data = json.dumps({'msg':'The required source is not available'})
                return self.render_to_http_response(json_data,status=404)
            json_data = self.serialize([cric,])
            return self.render_to_http_response(json_data)
        query_string = Cricketer.objects.all()
        json_data = self.serialize(query_string)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        ''' This function is used to insert the data into the DB '''
        data = request.body
        valid_json_data = is_valid_json_data(data)
        if not valid_json_data: 
            json_data = json.dumps({'msg':'Please Provide the Valid Json Data'})
            return self.render_to_http_response(json_data,status=400)
        
        provided_data = json.loads(data)
        form = CricketerForm(provided_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg' : 'The data is Valid ,resource got created'})
            return self.render_to_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        ''' This function is used to update the data in the DB '''
        data = request.body
        valid_json_data = is_valid_json_data(data)
        if not valid_json_data: 
            json_data = json.dumps({'msg':'Please Provide the Valid Json Data'})
            return self.render_to_http_response(json_data,status=400)
       
        #This is the data coming from Python application inorder to update
        provided_data = json.loads(data)
        id = provided_data.get('id',None)
        if id is None:
            json_data = json.dumps({'msg':'To perform Updation id is mandatory....  Please Provide the id'})
            return self.render_to_http_response(json_data,status=400)
        
        cric = self.get_object_data_by_id(id)
        if cric is None:
            json_data = json.dumps({'msg':'The required  source is not available'})
            return self.render_to_http_response(json_data,status=404)
        
        #this is the data which is been stored within the database
        original_data = {'name':cric.name,'jersey_number':cric.jersey_number,'age':cric.age,'ipl_team':cric.ipl_team}
        print('Data before Updation')
        print(original_data)
        
        print('Data After updation')
        original_data.update(provided_data)
        print(original_data)
        
        form = CricketerForm(original_data,instance=cric)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource Updated successfully'})
            return self.render_to_http_response(json_data)
    
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        ''' This function is used to delete the data from the DB '''
        data = request.body
        valid_json_data = is_valid_json_data(data)
        if not valid_json_data:
            json_data=json.dumps({'msg':'Please send the valid json data'})
            return  self.render_to_http_response(json_data,status=400)
        
        #This is the data coming from Python application inorder  to delete
        provided_data = json.loads(data)
        id = provided_data.get('id',None)
        if id is not None:
            cric = self.get_object_data_by_id(id)
            if cric is None:
                json_data = json.dumps({'msg':'No matched resource found, deletion not possible'})
                return self.render_to_http_response(json_data,status=404)
            
            (status,deleted_item) = cric.delete()
            if status == 1:
                json_data=json.dumps({'msg':'Resource deleted successfully'})
                return self.render_to_http_response(json_data)
                
            json_data=json.dumps({'msg':'Resource not deleted successfully'})
            return self.render_to_http_response(json_data)
            
        json_data=json.dumps({'msg':'To perform Deletion id is mandatory....Please Provide the id'})
        return self.render_to_http_response(json_data,status=400)