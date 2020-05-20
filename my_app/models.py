from django.db import models

# Create your models here.
#database model called search
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        #whatever the search field is there return it for me!
        return '{}'.format(self.search)
    
    #Meta for correct spelling as website adds 's' for plural so 'searchs' -> 'searches'
    #should be under 'search' class
    class Meta:
        verbose_name_plural = 'Searches'