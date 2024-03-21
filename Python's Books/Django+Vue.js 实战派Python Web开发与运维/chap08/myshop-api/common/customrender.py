from rest_framework.renderers import JSONRenderer
class CustomRender(JSONRenderer):
    def render(self,data,accepted_media_type=None,renderer_context=None):
        if renderer_context:
            if isinstance(data, dict):
                msg=data.pop('msg','请求成功')
                code=data.pop('code',renderer_context["response"].status_code)
                next=data.pop('next',data['next'])
                if 'results' in data:
                    data=data['results']
            else:
                #msg=renderer_context["response"].status_code
                #code=renderer_context["response"].status_text
                next=''          
            ret={
                    'code':renderer_context["response"].status_code,
                    'msg':renderer_context["response"].status_text,
                    'next':next,
                    'data':data,
                }
            return super().render(ret,accepted_media_type,renderer_context)
        else:
            return super().render(data,accepted_media_type,renderer_context)
