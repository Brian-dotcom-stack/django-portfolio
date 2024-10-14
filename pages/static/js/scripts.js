<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{% block title %}My Personal Portfolio{% endblock title %}</title>
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body class="container">
{% block page_content %}{% endblock page_content %}

<!-- Optional JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
<script src="{% static 'js/scripts.js' %}"></script>
</body>
</html>
