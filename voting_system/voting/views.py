# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Candidate, Vote
from .forms import CandidateForm, VoterRegistrationForm

# Voter registration view
from django.shortcuts import render, redirect
from .forms import VoterRegistrationForm

def voter_register(request):
    if request.method == 'POST':
        form = VoterRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect the user to the login page after successful registration
            return redirect('login')
    else:
        form = VoterRegistrationForm()

    return render(request, 'voting/voter_register.html', {'form': form})

# Voter home view
@login_required
def voter_home(request):
    candidates = Candidate.objects.all()
    return render(request, 'voting/voter_home.html', {'candidates': candidates})

# Voting view
@login_required  # Ensure the user is logged in
def vote(request, candidate_id):
    # Retrieve the candidate object
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == 'POST':
        # Increment the vote count for the candidate
        candidate.vote_count += 1
        # Save the candidate object
        candidate.save()
        # Redirect to the voter home page
        return redirect('voter_home')
    else:
        # If the request method is not POST, redirect to the voter home page
        return redirect('voter_home')

# Admin portal: List candidates
@login_required
def admin_candidates(request):
    candidates = Candidate.objects.all()
    return render(request, 'voting/admin_candidates.html', {'candidates': candidates})

# Admin portal: Create candidate
@login_required
def admin_create_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_candidates')
    else:
        form = CandidateForm()

    return render(request, 'voting/admin_create_candidate.html', {'form': form})

# Admin portal: View voters and votes
@login_required
def admin_votes(request):
    votes = Vote.objects.all()
    return render(request, 'voting/admin_votes.html', {'votes': votes})

def voter_home(request):
    # Retrieve all candidates from the database
    candidates = Candidate.objects.all()
    # Pass the candidates to the template
    return render(request, 'voting/voter_home.html', {'candidates': candidates})

def vote(request, candidate_id):
    # Get the candidate object based on the candidate_id
    candidate = get_object_or_404(Candidate, id=candidate_id)
    
    if request.method == 'POST':
        # Increment the vote count for the candidate
        candidate.vote_count += 1
        candidate.save()
        
        # Redirect back to the voter's home page
        return redirect('voter_home')

    # If the request method is not POST, redirect to the home page
    return redirect('voter_home')

def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == 'POST':
        candidate.vote_count += 1
        candidate.save()
        return redirect('voter_home')
    return redirect('voter_home')