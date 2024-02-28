userDB="hidrotech123"
passwordDB="admin123*"

print('software tech hidroituango')
print('**************************')
userName=input('Digitatu usuario: ')
userPassword=input('Digita tu contraseña:  ')

'''if userDB==userName and passwordDB==userPassword:
    print("Exito en su usario")
else:
    print("Fallaste")'''

print("Exito en su usario") if userDB==userName and passwordDB==userPassword else print("Fallaste")