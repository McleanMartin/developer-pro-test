from django.db import models

# Create your models here.


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    auto_now=False, auto_now_add=False)
    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})
