# Authenticated_Django_API

Authenticated Users can update the user's role or can see/ make changes on the api calls , whereas unauth user can only see the api calls

Tech:- Django , Inside Django (Custom Auth , Serialization , Routers, View Set
DB Tool -Postgres/SqlLite

EndPoints:-
1. http://127.0.0.1:8000/api/v1/ -  Home
2.- Companies Info - {Home}/companies
3.  Employee Info  - {Home}/employees
4. - Many to one Mapping - (Many(Employee) to One(Company) {Home}/companies/{id}/employees
5. - Custom Super-admin Functionalities .
