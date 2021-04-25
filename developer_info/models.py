from django.db import models

class Testimonial(models.Model):
    """Model for representing a testimonial"""
    quote = models.TextField(help_text="Enter the testimonial quote")
    author = models.CharField(max_length=200, help_text="Enter the author's name")
    job_title = models.CharField(max_length=200, help_text="Enter the author's title/description")

    class Meta:
        ordering = ['author']

    def __str__(self):
        return f'{self.author}, {self.job_title}'


class Project(models.Model):
    """Model for representing a project in a developer's portfolio"""
    name = models.CharField(max_length=200, help_text="Enter the project name")
    
    PROJECT_TYPES = (
        ('w', 'Website'),
        ('c', 'Code'),
    )


    project_type = models.CharField(
        max_length=1,
        choices=PROJECT_TYPES,
        blank=True,
        default='w',
        help_text='Project type',
    )
    
    description = models.TextField(help_text="Describe the project")
    url = models.URLField(null=True, blank=True, help_text="Enter the website or GitHub URL")
    thumbnail = models.ImageField(upload_to='images/', null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'



