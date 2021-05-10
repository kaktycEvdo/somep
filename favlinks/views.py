from django.http import HttpResponseRedirect, Http404
import pyrebase
from django.shortcuts import render
from requests.exceptions import HTTPError
import random
import collections
from urllib.parse import urlparse
from urllib.request import urlopen
from lxml.html import parse


config = {
    'apiKey': "AIzaSyD-7juj1qoLu3ZQHu4IVbhyc4w2AeCcVYQ",
    'authDomain': "itproject-bd975.firebaseapp.com",
    'projectId': "itproject-bd975",
    'storageBucket': "itproject-bd975.appspot.com",
    'messagingSenderId': "796204126281",
    'appId': "1:796204126281:web:ca2c78501254a9c246ef98",
    'measurementId': "G-MG0RB5T2XN",
    "databaseURL": "https://itproject-bd975-default-rtdb.firebaseio.com/",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
# https://itproject-bd975.firebaseapp.com/__/auth/handler


class Link:
    link = str
    color = str
    key = str
    netloc = str
    title = str


def main(request):
    check = 0
    m = collections.OrderedDict
    m1 = collections.defaultdict
    links = list({})
    l = int
    addb = int
    try:
        if request.method == "POST":
            email = request.POST.get('email')
            pswrd = request.POST.get('pswrd')
            request.session['email'] = email
            request.session['pswrd'] = pswrd

        if request.session['t'] == 'auth':
            request.session['user'] = auth.sign_in_with_email_and_password(request.session['email'], request.session['pswrd'])
        elif request.session['t'] == 'reg':
            user = auth.create_user_with_email_and_password(request.session['email'], request.session['pswrd'])
            request.session['user'] = auth.sign_in_with_email_and_password(request.session['email'], request.session['pswrd'])
        user = request.session['user']
        email = str(request.session['email'])
        email_m = email.split("@", 1)[0]
        stuff1 = db.child(email_m).get(user['idToken']).val()

    except(HTTPError):
        return HttpResponseRedirect('authorisation.html')

    user = request.session['user']
    if stuff1 is not None:
        m = dict(stuff1)
        keys = list(m.keys())
        for i in range(len(keys)):
            links.append(Link())
            links[i].link = m[keys[i]]['link']
            links[i].color = m[keys[i]]['color']
            links[i].key = keys[i]
            page = urlopen(links[i].link)
            p = parse(page)
            links[i].title = p.find(".//title").text
            parsed_uri = urlparse(m[keys[i]]['link'])
            result = '{uri.netloc}'.format(uri=parsed_uri)
            links[i].netloc = result
        addb = int(str(keys[len(keys)-1])[2:])
        addb+=1

    return render(request, 'favlinks/main.html', {"links": links, "addb": addb, "email": email})


def authorisation(request):
    request.session['t'] = 'auth'
    return render(request, 'favlinks/authorisation.html')


def registration(request):
    request.session['t'] = 'reg'
    return render(request, 'favlinks/registration.html')


def change_content(request):
    try:
        user = request.session['user']
        email = str(request.session['email'])
        email = email.split("@", 1)[0]

        str1 = request.session['id']

        if request.session['t'] == 'add':
            db.child(email).child(str1).child('link').set(request.POST['link'], user['idToken'])
            random_number = random.randint(0,16777215)
            hex_number = format(random_number, 'x')
            hex_number = '#' + hex_number
            db.child(email).child(str1).child('color').set(hex_number, user['idToken'])
        if request.session['t'] == 'edit':
            db.child(email).child(str1).child('link').set(request.POST['link'], user['idToken'])
        if request.session['t'] == 'remove':
            db.child(email).child(str1).remove(user['idToken'])

    except(HTTPError):
        return HttpResponseRedirect('main.html')
    return HttpResponseRedirect('main.html')


def add(request):
    request.session['t'] = 'add'
    request.session['id'] = request.GET['id']
    email = str(request.session['email'])

    return render(request, 'favlinks/add.html', {"email": email})


def edit(request):
    request.session['t'] = 'edit'
    request.session['id'] = request.GET['id']
    email = str(request.session['email'])

    return render(request, 'favlinks/edit.html', {"email": email})


def delete(request):
    request.session['t'] = 'remove'
    request.session['id'] = request.GET['id']

    return render(request, 'favlinks/delete.html')


# что возможно войдет в дипломную
# def get(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     self.form = self.get_form(form_class)
    #
    #     self.object_list = self.get_queryset()
    #     allow_empty = self.get_allow_empty()
    #     if not allow_empty and len(self.object_list) == 0:
    #         raise Http404("Empty list and '"+self.__class__.__name__+"s.allow_empty' is False.")
    #
    #     context = self.get_context_data(object_list=self.object_list, form=self.form)
    #     return self.render_to_response(context)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.get(request, *args, **kwargs)
# class FavlinkCreate(generic.CreateView):
#     model = Links
#     form_class = BookmarkForm
#     template_name = 'favlinks/add.html'
#     context_object_name = 'form'
#
#
# class FavlinkUpdate(generic.UpdateView):
#     model = Links
#     form_class = BookmarkForm
#     template_name = 'favlinks/edit.html'
#     context_object_name = 'form'
#
#
# class FavlinkDelete(generic.DeleteView):
#     model = Links
#     template_name = 'favlinks/delete.html'
#     context_object_name = 'form'
#     success_url = reverse_lazy('favlinks:favlinks')
#
#
# class AuthorisationView(generic.edit.FormView, FormMixin):
#     model = User
#     form_class = AuthorisationForm
#     context_object_name = 'form'
#     template_name = 'favlinks/authorisation.html'
#     success_url = "/favlinks/"
#
#     def form_valid(self, form):
#         User.is_authorised = True
#
#         return super(AuthorisationView, self).form_valid(form)
#
#
# class RegistrationView(generic.CreateView, FormMixin):
#     model = User
#     context_object_name = 'form'
#     form_class = RegistrationForm
#     template_name = 'favlinks/registration.html'
#     success_url = '/favlinks/'
#
#     def form_valid(self, form):
#         form.save()
#         User.is_authorised = True
#
#         return super(RegistrationView, self).form_valid(form)
# class FavlinksView(generic.ListView):
#     model = Links
#     template_name = 'favlinks/main.html'
#     context_object_name = 'links'
#     object_list = model.objects
#
#     user = auth.sign_in_with_email_and_password(str(model.user.email), str(model.user.password))
#
#     def get_queryset(self):
#         if Links.user:
#             return Links.objects.filter(user__username=Links.user)
# firebase deploy чтобы выложить всё в хостинг
