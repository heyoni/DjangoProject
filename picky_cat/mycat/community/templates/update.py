{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}

<div style="text-align: center; max-width: 400px; margin: 4rem auto;">
    <div class="mb-4">
        <h2>수 정</h2>
    </div>
    # <form action="{% url 'profileapp:update' pk=target_profile.pk %}" method="POST" enctype="multipart/form-data">
    #     {% csrf_token %}
    #     {% bootstrap_form form %}
    #     <input type="submit" value="수정하기" class="btn btn-dark rounded-pill col-6 mt-3">
    # </form>
</div>

{% endblock %}