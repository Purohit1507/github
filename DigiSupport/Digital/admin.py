from django.contrib import admin
from.models import Post, NetAuthorizationRequest

@admin.register(Post)
class PostmodelAdmin(admin.ModelAdmin):
    list_display = ['id','department','Problem']
    
@admin.register(NetAuthorizationRequest)
class NetAuthorizationRequestAdmin(admin.ModelAdmin):
    list_display = [
        'applicant_ps_number', 'applicant_name', 'applicant_email_id',
        'request_date', 'location', 'department', 'contact_no',
        'initiator_hod_ps_no', 'initiator_hod_name', 'initiator_hod_email_id',
        'net_request_type', 'copy_to_id', 'copy_from_id',
        'application_name', 'justification'
    ]
