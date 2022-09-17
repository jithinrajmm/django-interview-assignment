from rest_framework import serializers
from users.models import User,Books
# validation erros in serilizer


class LibrarianSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password','is_librarian']
        # defining the password feild is not showed to the user
        # after registrations
        extra_kwargs = {
            'password':{ 'write_only':True },
            'is_librarian':{'write_only':True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        name = validated_data.get('name')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            # hashing the password
        instance.username=name
        instance.is_librarian=True
        instance.save()
        return instance
        
        
class MemberSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password','is_memeber']
        # defining the password feild is not showed to the user
        # after registrations
        extra_kwargs = {
            'password':{ 'write_only':True }
        }
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        name = validated_data.get('name')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            # hashing the password
        instance.username=name
        instance.is_memeber=True
        instance.save()
        return instance
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','name']
        