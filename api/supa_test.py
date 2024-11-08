import hashlib

from supabase import create_client, Client

#Supabase data connection: URL KEY
SUPABASE_URL="https://upecrltnenpemwjfdwyu.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVwZWNybHRuZW5wZW13amZkd3l1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY2NDYsImV4cCI6MjA0NTc0MjY0Nn0.xcQluJwp4ANHU3SZRf8wPcK5huGnJaf_yaYXyXuj2Is"

#Connect to Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

#Get and save data function
def  save_data(e, p):
    # Insert into users model
    enc_pass = hashlib.sha256(p.encode()).hexdigest()
    
    response = supabase.table('users').insert({"email": e, "password": enc_pass}).execute()
    
    if response.data:
        print(f"user has been save succesfully {response.data}")
    elif response.error:
        print(f"Error saving user: {response.error}")
    
#Main
email = input("User e-mail:")
passwd =input("User password:")
save_data(email, passwd)