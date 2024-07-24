import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
from project.empty import calculate_empty_percentage
from project.empty import calculate_below_ten_percentage
import os
from project.price import price

if __name__ == "__main__":
    column_name = 'review_count'  # Update with the actual column name
    homsa = pd.read_csv('data\homsa_data_v3 (2).csv',usecols=['review_count','city','price'])
    jajiga=pd.read_csv("data\jajiga_data (2).csv",usecols=['review_count','city','price'])
    otaghak=pd.read_csv("data\otaghak_V3_data (2).csv",usecols=['review_count','city','price'])
    shab=pd.read_csv("data\shab_data (2).csv",usecols=['review_count','city','price'])

    #empty and less than 10
    column_name = 'review_count'  # Update with the actual column name
    homsa = pd.read_csv('data\homsa_data_v3 (2).csv',usecols=['review_count','city','price',"overall_rate"])
    jajiga=pd.read_csv("data\jajiga_data (2).csv",usecols=['review_count','city','price','overall_rate'])
    otaghak=pd.read_csv("data\otaghak_V3_data (2).csv",usecols=['review_count','city','price','overall_rate'])
    shab=pd.read_csv("data\shab_data (2).csv",usecols=['review_count','city','price','overall_rate'])
    empty_percentage_jajiga = calculate_empty_percentage(jajiga, column_name)
    empty_percentage_shab = calculate_empty_percentage(shab, column_name)
    empty_percentage_otaghak = calculate_empty_percentage(otaghak, column_name)
    empty_percentage_homsa = calculate_empty_percentage(homsa, column_name)


    ten_percentage_jajiga =calculate_below_ten_percentage(jajiga, column_name)
    ten_percentage_shab = calculate_below_ten_percentage(shab, column_name)
    ten_percentage_otaghak = calculate_below_ten_percentage(otaghak, column_name)
    ten_percentage_homsa = calculate_below_ten_percentage(homsa, column_name)

    platform=["shab <10","jajiga <10", "otaghak <10","homsa <10"]
    plat=["shab","jajiga","otaghak","homsa"]
    a=[ten_percentage_shab,ten_percentage_otaghak,ten_percentage_jajiga,ten_percentage_homsa]
    a2=[empty_percentage_shab,empty_percentage_otaghak,empty_percentage_jajiga,empty_percentage_homsa]
    style.use("ggplot")
    plat=np.arange(len(plat)) 
    plt.figure(figsize=(40,7))
    barwidth=0.2
    plt.bar(plat,a,width=barwidth,color="royalblue",label="less than 10")
    plt.bar(plat+0.2,a2,width=barwidth,color="indigo",label="empty")
    plt.xticks(plat+0.1,("shab","jajiga","otaghak","homsa"),rotation=30,fontsize=12,color="black")
    plt.legend()
    lst=[ten_percentage_shab,empty_percentage_shab,ten_percentage_otaghak,empty_percentage_otaghak,ten_percentage_jajiga,empty_percentage_jajiga,ten_percentage_homsa,empty_percentage_homsa]
    cnt=0
    x=0
    for i in lst:
        plt.text(x, i+1, f"{i:.2f}%", horizontalalignment='center',
     verticalalignment='center')
        if cnt %2==0:
            x+=0.22
        else:
            x+=0.79
        cnt+=1
    
    result_dir = "result\empty and less than 10 review"
    file_path = os.path.join(result_dir, "empty and less than 10 review")
    plt.savefig(file_path)


    #price
    price(homsa,"homsa")
    price(jajiga,"jajiga")
    price(otaghak,"otaghak")
    price(shab,"shab")

