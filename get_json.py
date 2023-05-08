import requests
import json

def get_json(explanation):
    url = "https://prepai-generate-questions.p.rapidapi.com/getQuestions"

    # payload = "topic=Euler%20lagrange&content=The%20Euler-Lagrange%20equation%20is%20a%20mathematical%20equation%20used%20to%20find%20the%20path%20a%20system%20takes%20between%20two%20points%20in%20space%20and%20time%2C%20given%20a%20Lagrangian%20function%20that%20describes%20the%20system's%20energy.%20In%20this%20particular%20case%2C%20the%20Lagrangian%20function%20is%20defined%20as%200.5%20times%20the%20mass%20times%20the%20square%20of%20the%20velocity%20minus%20the%20potential%20energy.%20The%20partial%20derivative%20of%20the%20Lagrangian%20with%20respect%20to%20the%20velocity%20yields%20the%20momentum.%20The%20time%20derivative%20of%20the%20momentum%20yields%20the%20force%20acting%20on%20the%20system.%20The%20partial%20derivative%20of%20the%20Lagrangian%20with%20respect%20to%20the%20position%20yields%20the%20derivative%20of%20the%20potential%20energy.%20By%20substituting%20these%20values%20into%20the%20Euler-Lagrange%20equation%2C%20one%20can%20obtain%20an%20equation%20of%20motion%20for%20the%20system%2C%20which%20in%20this%20case%20corresponds%20to%20Newton's%20second%20law%20of%20motion."

    input_topic = "Sample topic"   
    payload = (
        f"topic={input_topic.replace(' ','%20')}&content={explanation.replace(' ','%20')}"
    )
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "d689751cb6msh89a2b50bf794f3fp101c6ajsnd1779857b5a5",
        "X-RapidAPI-Host": "prepai-generate-questions.p.rapidapi.com",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()

    # with open("sample.json", "w") as myfile:
    #     json.dump(response.json(), myfile)
