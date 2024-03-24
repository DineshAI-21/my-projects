"""
URL configuration for shopkart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



    ''' {% for item in products %}
            <div class="col-md-4 col-lg-3">
              <div class="card my-3">
                <img src="{{ item.product_image.url }}" alt="Categories" class="card-image-top">
                <hr style="border-color:#b8bfc2;">
                <a href="{% url 'collections' item.name %}">
                <div class="card-body">
                  <h5 class="card-title text-primary">{{ item.name }}</h5>
                  <p class="card-text">
                   <span class="float-start oldprice"><s>Rs.{{ item.original_price | stringformat:'d' }}</s></span>
                    <span class="float-end newprice">Rs.{{ item.selling_price | stringformat:'d'}}</span>
                  </p>
                  
                </div>
                </a>
              </div>
            </div>
            {% endfor %}'''