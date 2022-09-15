from model import reccom
import torch
import pandas as pd
import numpy as np
df = pd.read_csv("rating.csv")
df["userId"] -= 1
all_movieid = pd.read_csv("https://raw.githubusercontent.com/ohmreborn/CatMov-Website/main/movie.csv")
all_movieid["ai_id"] = list(range(len(all_movieid["movieId"])))
df = df.merge(all_movieid[['movieId', 'ai_id']], left_on='movieId',right_on='movieId', how='left')
df = df.merge(all_movieid[['movieId', 'title']], left_on='movieId',right_on='movieId', how='left')

def reccommend(id):
      new_model = reccom()
      new_model.load_state_dict(torch.load("sample_model_002"))

      #all mov user already watch
      watch = df[df["userId"] == id]["ai_id"]
      watch =watch.tolist()
      # mov
      mov_id = all_movieid["ai_id"].tolist()
      mov_id = np.array([mov_id])
      mov_id = np.delete(mov_id,watch)
      # not watch
      mov_id_2 = mov_id.reshape(1,len(mov_id))
      # user
      user_id =  np.zeros((1,len(mov_id))) + id

      data = np.concatenate((user_id,mov_id_2))
      data = data.T 
      data = torch.LongTensor(data)

      pred = new_model(data)
      pred = pred.detach()
      pred = pred.numpy()

      Data = {"ai_id":mov_id,
            "predict_rating":pred.flatten()}
      table = pd.DataFrame(Data)
      table.sort_values(by="predict_rating",inplace=True, ascending=False)
      output = pred = table.iloc[:10]
      output = output.merge(all_movieid[['ai_id', 'title']], left_on='ai_id',right_on='ai_id', how='left')
      return output["title"].tolist()

def return_to_user(mov_name,rating):
    all_user = df[df["title"]==mov_name]
    all_rating = all_user["rating"]-rating
    all_rating = all_rating**2
    all_user.loc[:,"error"] = all_rating
    all_user.sort_values(by='error', inplace=True)

    userID = all_user["userId"].tolist()
    userID = userID[0]
    
    return reccommend(userID)
print(return_to_user("Avatar (2009)",0))