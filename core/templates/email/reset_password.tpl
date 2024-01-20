{% extends "mail_templated/base.tpl" %}

{% block subject %}
Rest Password
{% endblock %}

{% block html %}
<a href="http://127.0.0.1:8000/accounts/api/v1/reset-password-confirm/{{token}}">Rest your password with this url</a>

</br>
<img 
    src="https://dfstudio-d420.kxcdn.com/wordpress/wp-content/uploads/2019/06/digital_camera_photo-980x653.jpg"
    width="500px">
<img 
    src="https://webneel.com/wallpaper/sites/default/files/images/08-2018/3-nature-wallpaper-mountain.1024.jpg"
    width="500px">
    
{% endblock %}