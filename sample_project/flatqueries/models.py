from django.db import models

MAX_QUERY_TITLE = 50

class Query(models.Model):
    title = models.CharField(blank=False, null=False, max_length=MAX_QUERY_TITLE,
        help_text='Short, simple, easy-to-remember title')
    description = models.TextField(blank=True, null=True)
    sql = models.TextField(blank=False, null=False)

    @models.permalink
    def get_absolute_url(self):
        return ('flatqueries.views.run', (), { 'id': str(self.id) })
        
    class Meta:
        verbose_name = 'flat query'
        verbose_name_plural = 'flat queries'


