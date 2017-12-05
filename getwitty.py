from wit import Wit

client = Wit(access_token = "IWNYQ6NNI5N5PCHYGSNZGPLZPAP3OJT2")


def wit_response(message_text):
    resp = client.message(message_text)
    try:
        categories = {}
        entities = list(resp['entities'])
        #print(entities)
        if "greetings" in entities:
         #   print("here")
            return "greeting"
        else:
          #  print("and else")
            for entity in entities:
                print(entity)
                categories[entity] = resp['entities'][entity][0]['value']
            print(categories)
            return categories[entity]
    except:
        pass


