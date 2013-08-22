'''
Created on 22.08.2013

@author: Dmitry
''' 
   

#existMarker = '[SoapExtensionLib.ProgressExtension]public AtttachmentLoaded GetAttachment('
extension = '[SoapExtensionLib.ProgressExtension]'
beforeMarker = 'public AtttachmentLoaded GetAttachment('
filename = 'D:\\projects\\branch\\ultima_ios\\UltimaSigneeDroid\\Web References\\MobileWeb\\Reference.cs' 

#filename = re.escape(filename)

f = open(filename)
lines = f.readlines()
f.close()

f = open(filename, 'w')
existmarker = extension + beforeMarker 
for s in lines:
    if existmarker not in s:
        if beforeMarker in s:
            print 'Found and replacing'
            s = s.replace(beforeMarker, existmarker)
    else:    
        print 'Already have', extension            
    
        
    f.write(s)
f.close()   
