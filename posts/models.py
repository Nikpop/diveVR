from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    background = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_detail', args=[str(self.id)])


    def product_register_disable(request):
        product_id = request.POST.get('productregister_id') # The variable sent from javascript in request object is captured in product_id variable in python function.

    # From here you can use this variable (product_id) in your python function.

        product_instance = Productregister.objects.get(id=product_id)

        if product_instance.product_status == "active":
           product_instance.product_status = "deactive"
           product_status = "deactive"
           product_instance.save()
           return render(request, 'productregister/product_status.html', {'product_status': product_status})

        else:
          product_instance.product_status = "active"
          product_status = "active"
          product_instance.save()
          return render(request, 'productregister/product_status.html', {'product_status': product_status})
