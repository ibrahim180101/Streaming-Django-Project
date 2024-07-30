from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from .models import MainsectionMovie,MainsectionSeries
import razorpay

#for register
def register(request):
    b = {}
    if request.method == 'POST':
        u = request.POST['uname']
        l = request.POST['uemail']
        p = request.POST['upass']
        cp = request.POST['ucpass']
        
        if u == '' or l == '' or p == '' or cp == '':
            b['err'] = 'The fields cannot be empty'
            return render(request, 'register.html', b)
        elif p != cp:
            b['err'] = 'Passwords did not match'
            return render(request, 'register.html', b)
        else:
            try:
                a = User.objects.create_user(username=u, email=l, password=p)
                a.save()
                b['success'] = "Successfully registered"
                return redirect('/login/')  # Update this to the appropriate URL
            except:
                b['err'] = "User already exists"
                return render(request, 'register.html', b)
    else:
        return render(request, 'register.html', b)


#for login
def user_login(request):
    a = {}
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST['uname']  
        p = request.POST['upass']
        
        if u == '' or p == '':
            a['err'] = "Fields cannot be empty"
            return render(request, 'login.html', a)
        else:
            user = authenticate(username=u, password=p)
            if user is not None:
                login(request, user)
                return redirect('/moviepage/') 
            else:
                a['err'] = "Invalid credentials"
                return render(request, 'login.html', a)

#for logout
def user_logout(request):
        logout(request)
        return redirect('/login/')

# for home page
def home(request):
    movieall = MainsectionMovie.objects.all()[6:14]
    seriesall=MainsectionSeries.objects.all()[12:20]
    context = {
        'movieall':movieall,
        'seriesall': seriesall

    }
    return render(request, 'Home.html', context)
#for movie page
def moviessection(request):
    all=MainsectionMovie.objects.all()
    action_movies = MainsectionMovie.objects.filter(genre=1) # Assuming '1' corresponds to Action and Adventure
    comedy_movies= MainsectionMovie.objects.filter(genre=2)
    drama_movies = MainsectionMovie.objects.filter(genre=3) # Assuming '3' corresponds to Drama
    horror_movies= MainsectionMovie.objects.filter(genre=4)
    romance_movies= MainsectionMovie.objects.filter(genre=5)
    kids_movies= MainsectionMovie.objects.filter(genre=6)
    mysteryandthrillers= MainsectionMovie.objects.filter(genre=7)
    scifi= MainsectionMovie.objects.filter(genre=8)
   
    context = {
        'action_movies': action_movies,
        'drama_movies': drama_movies,
        'comedy_movies':comedy_movies,
        'horror_movies':horror_movies,
        'romance_movies':romance_movies,
        'kids_movies':kids_movies,
        'mysteryandthrillers':mysteryandthrillers,
        'scifi':scifi,
        'all':all
    }

    return render(request, 'moviesection.html', context)
# for series page
def tvshowssection(request):
    awardwin = MainsectionSeries.objects.filter(genre=1)  # Assuming '1' corresponds to Award-Winning Tv Shows
    Epicworlds = MainsectionSeries.objects.filter(genre=2)  # Assuming '2' corresponds to Epic worlds
    Excitingtv = MainsectionSeries.objects.filter(genre=3)  # Assuming '3' corresponds to Exciting Tv shows
    Marvel = MainsectionSeries.objects.filter(genre=4)  # Assuming '4' corresponds to Marvel Tv shows
    context = {
        'awardwin': awardwin,
        'Epicworlds': Epicworlds,
        'Excitingtv': Excitingtv,
        'Marvel': Marvel,
    }
    return render(request, 'seriessection.html', context)




# to show seperate sections
def action(request):
    action_movies = MainsectionMovie.objects.filter(genre=1)
    context = {
          'action_movies': action_movies,
      }
    return render(request, 'action.html', context)

def horror(request):
    horror_movies= MainsectionMovie.objects.filter(genre=4)
    context = {
         'horror_movies':horror_movies,
      }
    return render(request, 'Horror.html', context)
def comedy(request):
    comedy_movies= MainsectionMovie.objects.filter(genre=2)
    context = {
        'comedy_movies':comedy_movies,
      }
    return render(request, 'comedy.html', context)
def drama(request):
    drama_movies = MainsectionMovie.objects.filter(genre=3) 
    context = {
       'drama_movies': drama_movies,
      }
    return render(request, 'drama.html', context)
def romance(request):
    romance_movies= MainsectionMovie.objects.filter(genre=5)
    context = {
       'romance_movies':romance_movies,
      }
    return render(request, 'romance.html', context)
def kids(request):
    kids_movies= MainsectionMovie.objects.filter(genre=6)
    context = {
       'kidsmovies':kids_movies,
      }
    return render(request, 'kids.html', context)
def mystery(request):
    mysteryandthrillers= MainsectionMovie.objects.filter(genre=7)
    context = {
       'mysteryandthrillers':mysteryandthrillers,
      }
    return render(request, 'mystery.html', context)
def scifi(request):
    scifi= MainsectionMovie.objects.filter(genre=8)
    context = {
       'scifi':scifi,
      }
    return render(request, 'scifi.html', context)



#for showing details of series and movies
def series_detail(request, id):
    series = get_object_or_404(MainsectionSeries, id=id)
    return render(request, 'seriesdetails.html', {'series': series})

def movie_detail(request, id):
    movies = get_object_or_404(MainsectionMovie, id=id)
    return render(request, 'moviesetails.html', {'movies': movies})




#for showing videos of both page
def watchvideo(request, id):
    movie = get_object_or_404(MainsectionMovie, id=id)
    return render(request, 'movievideo.html', {'movie': movie})

def watchseries(request, id):
    series = get_object_or_404(MainsectionSeries, id=id)
    return render(request, 'seriesvideo.html', {'series': series})

#payments and plans
from django.shortcuts import render
import razorpay

# Initialize Razorpay client with your key and secret
razorpay_client = razorpay.Client(auth=("rzp_test_W1F1EWIPGpmCRP", "aLdEEIU85UXDYBeBqRICZIco"))

def plans_view(request):
    plans = [
        {
            'id': 'premium',
            'name': 'Premium',
            'description': '4K + HDR',
            'price': 649,
            'quality': 'Best',
            'resolution': '4K (Ultra HD) + HDR',
            'devices': 'TV, computer, mobile phone, tablet',
            'simultaneous_streams': 4
        },
        {
            'id': 'standard',
            'name': 'Standard',
            'description': '1080p',
            'price': 499,
            'quality': 'Great',
            'resolution': '1080P (Full HD)',
            'devices': 'TV, computer, mobile phone, tablet',
            'simultaneous_streams': 2
        },
        {
            'id': 'basic',
            'name': 'Basic',
            'description': '720p',
            'price': 199,
            'quality': 'Good',
            'resolution': '720p (HD)',
            'devices': 'TV, computer, mobile phone, tablet',
            'simultaneous_streams': 1
        }
    ]
    return render(request, 'plans.html', {'plans': plans})

def payment_view(request, plan_id, amount):
    # Create an order in Razorpay
    order_amount = amount * 100  # Convert to subunits
    order_currency = 'INR'
    order_receipt = f'order_rcptid_{plan_id}'
    notes = {'plan': plan_id}

    order = razorpay_client.order.create({
        'amount': order_amount,
        'currency': order_currency,
        'receipt': order_receipt,
        'notes': notes
    })

    context = {
        'amount': order_amount,
        'order_id': order['id'],
        'plan': plan_id
    }
    return render(request, 'payment.html', context)





















