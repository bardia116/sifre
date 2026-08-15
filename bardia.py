import streamlit as st
import string
import random

isim=st.text_input("isim giriniz ")
soyisim=st.text_input("Soyisim Giriniz ")
domain=st.selectbox("domain seçiniz",("finis.com.tr","finiscode.com"))

basharf=isim[0:2]

email=basharf+"."+soyisim+"@"+domain

email=email.lower()
email=email.replace("ç","c")
email=email.replace("ı","i")
email=email.replace("ğ","g")
email=email.replace("ü","u")
email=email.replace("ö","o")
email=email.replace("ş","s")


bhsec=''.join(random.choices(string.ascii_uppercase,k=2))
khsec=''.join(random.choices(string.ascii_lowercase,k=2))
dgsec=''.join(random.choices(string.digits,k=2))
sysec=''.join(random.choices(string.punctuation,k=2))

sifre=basharf+bhsec+khsec+dgsec+sysec
random.shuffle(sifre)
sifre="".join(sifre)


st.write(email)
st.write(sifre)
st.button("yenile")