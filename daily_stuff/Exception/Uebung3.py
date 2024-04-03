import logging
values =[10,5,6,0,9,8,"Hello",2]

for value in values:
    try:
        print(10/ int(value))
        raise AttributeError #Hello world wird jedesmal aufgerufen-> öffnet den ecept attributeError block
    except (ValueError,ZeroDivisionError) as e:
        #pass #überspringt error meldungen
        print(e) #zeigt error meldungen
    except AttributeError as e:
        print("Hello World")
        continue
    except Exception as e:
        looging.exception(e)