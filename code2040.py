import requests
r = requests.post('http://challenge.code2040.org/api/register', data = {'token':'956ad89ae9305e9ce01fb11880df9def', "github":"https://github.com/liveSisu/code2040fellows"})
print (r)

