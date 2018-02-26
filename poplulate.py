import factory  
import factory.django
from toy.models import Cases

class UserFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = Cases
    caseTitle = factory.Faker('name')
    body = factory.Faker('sentence')
    DOJ = factory.Faker('date')


