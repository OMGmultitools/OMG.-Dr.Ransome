#!/usr/bin/python3

try :
    import nacl, nacl,secret,pathlib, os
except :
    print("Error run pip install requirements.txt")


    """Making class in order decrypt"""

    class Decrypt(Object):

        def __init__(self, Target,BoxM):
            self.Target = Target
            self.BoxM

            def FileE(loc):
                DefFileN  = (loc.Target).strip(.lol)
                EnFileN   = (loc.Target)
                Date      = 0

                with open(EnFileN,"rb") as File: Date = File.Read()
                Decrypted     = loc.BoxM.decrypt(Date)
                os.remove(EnFile)
                print(f"Decrypet --> {DefileN}")

                """Settings Up Some Global Vaes"""

                Key   = b'YOUR KEY'
                box   = nacl.secret.SecretBox(Key)
                paths = [r"C:\Users\\"]
                
                """Our ForLoop So we walkthrought Our paths"""

                for allfiles in paths :
                   if (pathlib.Path(AllFiles).exists()):
                       for path, subdirs, files in os.walk(AllFiles):
                            if(("\\AppData\\") in path):pass
                            else:
                                for file in files :
                                    if(".lol" in file):
                                        FilePath    = os.path.join(path, file)  
                                        Decrypt(FilePath,box).FileE()