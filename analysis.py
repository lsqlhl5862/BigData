import pandas as pd
from matplotlib import pyplot as plt
from functools import cmp_to_key
plt.style.use("ggplot")

result = {}
df = pd.read_csv("results/result_"+"crypto"+".csv", index_col=0)
result['crypto'] = pd.read_csv("results/result_"+"crypto"+".csv", index_col=0)
result['fs'] = pd.read_csv("results/result_"+"fs"+".csv", index_col=0)
result['ipc'] = pd.read_csv("results/result_"+"ipc"+".csv", index_col=0)
result['kvm'] = pd.read_csv("results/result_"+"kvm"+".csv", index_col=0)
result['md'] = pd.read_csv("results/result_"+"md"+".csv", index_col=0)
result['mm'] = pd.read_csv("results/result_"+"mm"+".csv", index_col=0)


def cutTime(df):
    list = df["editTime"].split("-", 2)
    return list[0]+"-"+list[1]

def cmpVersion(a):
    tempA = a.split(".")
    lenA=len(tempA)
    sum=0
    for i in range(lenA):
        sum+= int(tempA[i])*(10**(9-3*i))
    return sum


date = df.apply(cutTime, axis=1)

df["editTime"] = date
df["patchName"] = df.apply(lambda x: x["patchName"].split("-")[1], axis=1)
list=df["patchName"].tolist()
list.sort(key=cmpVersion)
df['patchName'] = df['patchName'].astype('category')
df['patchName'].cat.reorder_categories(list, inplace=True)
df.sort_values('patchName', inplace=True)
df=df.reset_index()
version=pd.DataFrame(df["patchName"].values.tolist())
version.to_csv("results/version.csv")
# print(df["patchName"].values.tolist())


for item in result:
    result[item]["editTime"] = date
    result[item]["patchName"] = result[item].apply(
        lambda x: x["patchName"].split("-")[1], axis=1)
    result[item]['patchName'] = result[item]['patchName'].astype('category')
    result[item]['patchName'].cat.reorder_categories(list, inplace=True)
    result[item].sort_values('patchName', inplace=True)
    result[item]=result[item].reset_index()
    # print(result[item])


# # print(df.groupby(["editTime"]).size().values)
# # patch次数
# plt.figure()
# plt.bar(df.groupby(["editTime"]).size().index.tolist()[:48],df.groupby(["editTime"]).size().values.tolist()[:48])
# plt.gcf().autofmt_xdate()
# plt.xticks(fontsize=5)
# plt.yticks(fontsize=20)
# plt.xlabel("date", fontsize=10)
# plt.ylabel("times", fontsize=10)
# plt.title("Patch Counts of Every Month-1")
# plt.savefig("pictures/"+"patch-time-1.png")
# # print(df.groupby(["editTime"]).size().values)
# # patch次数
# plt.figure()
# plt.bar(df.groupby(["editTime"]).size().index.tolist()[48:],df.groupby(["editTime"]).size().values.tolist()[48:])
# plt.gcf().autofmt_xdate()
# plt.xticks(fontsize=5)
# plt.yticks(fontsize=20)
# plt.xlabel("date", fontsize=10)
# plt.ylabel("times", fontsize=10)
# plt.title("Patch Counts of Every Month-2")
# plt.savefig("pictures/"+"patch-time-2.png")

# # print(df.apply(lambda x:x["diffCount"]/x["count"],axis=1).values)

# # # diff占比
# for item in result:
#     plt.figure()
#     x=range(832)
#     y=result[item].apply(lambda x:x["diffCount"]/x["count"],axis=1).values
#     plt.plot(x,y)
#     plt.gcf().autofmt_xdate()
#     plt.xticks(fontsize=5)
#     plt.yticks(fontsize=10)
#     plt.xlabel("version", fontsize=10)
#     plt.ylabel("times", fontsize=10)
#     plt.title("Diff Proportion of Every Patch"+" About "+item)
#     plt.savefig("pictures/"+"diffCount_"+item+".png")

# # # 修改数量
# for item in result:
#     plt.figure()
#     x=range(832)
#     y = result[item].apply(lambda x: x["editCount"], axis=1).values
#     plt.plot(x, y)
#     plt.xticks(fontsize=5)
#     plt.yticks(fontsize=10)
#     plt.xlabel("version", fontsize=10)
#     plt.ylabel("times", fontsize=10)
#     plt.title("EditCounts of Every Patch"+" About "+item)
#     plt.savefig("pictures/"+"EditCounts_"+item+".png")


# # patch格式占比
# plt.figure()
# labels = 'HaveTime','HaveIndex','Double lose'
# sizes = [df.loc[df["haveTime"]==True,:].loc[df["haveIndex"]==False,:].shape[0],df.loc[df["haveTime"]==False,:].loc[df["haveIndex"]==True,:].shape[0],df.loc[df["haveTime"]==False,:].loc[df["haveIndex"]==False,:].shape[0]]
# explode = (0,0.1,0)
# plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90) #startangle表示饼图的起始角度
# plt.axis('equal')
# plt.savefig("pictures/"+"patch_format.png")

#patch大小随时间变化

# df_size=pd.read_csv("results/result_"+"crypto"+".csv", index_col=0)
# df_size.sort_values(by=["editTime"],ascending=True)
# plt.figure()
# plt.bar(range(832),df_size["size"].values)
# plt.gcf().autofmt_xdate()
# plt.xticks(fontsize=5)
# plt.yticks(fontsize=20)
# plt.xlabel("version", fontsize=10)
# plt.ylabel("size", fontsize=10)
# plt.title("Size of Version")
# plt.savefig("pictures/"+"size-version.png")
# print(df.groupby(["editTime"])["size"].size())

# 大小随版本变化
# plt.figure()
# plt.bar(range(832),df["size"].values)
# plt.gcf().autofmt_xdate()
# plt.xticks(fontsize=5)
# plt.yticks(fontsize=20)
# plt.xlabel("version", fontsize=10)
# plt.ylabel("times", fontsize=10)
# plt.title("Size of Version")
# plt.savefig("pictures/"+"size-version.png")



# # # 最大修改行数
# plt.figure()
# for item in result:
#     x=range(832)
#     y = result[item].apply(lambda x: x["maxChangeLine"], axis=1).values
#     plt.plot(x, y,"--",label=item)
# plt.xticks(fontsize=5)
# plt.yticks(fontsize=10)
# plt.xlabel("version", fontsize=10)
# plt.ylabel("lines", fontsize=10)
# plt.title("MaxChangeLine for Versions")
# plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)
# plt.savefig("pictures/"+"maxChangeLine_version.png")
# plt.show()

# # 修改行数
# for item in result:
#     plt.figure()
#     x=range(832)
#     y1=result[item].apply(lambda x:x["subCount"],axis=1).values
#     y2=result[item].apply(lambda x:x["addCount"],axis=1).values
#     y3=result[item].apply(lambda x:x["annotationCount"],axis=1).values
#     plt.plot(x,y1,"--",label="subCount")
#     plt.plot(x,y2,"--",label="addCount")
#     plt.plot(x,y3,"--",label="annotationCount")
#     plt.gcf().autofmt_xdate()
#     plt.xticks(fontsize=5)
#     plt.yticks(fontsize=10)
#     plt.xlabel("version", fontsize=10)
#     plt.ylabel("times", fontsize=10)
#     plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)
#     plt.title("Changelines of Every Version"+" About "+item)
#     plt.savefig("pictures/"+"Changelines_"+item+".png")

# # 修改行数
# plt.figure()
# for item in result:
#     x=range(832)
#     y = result[item].apply(lambda x: x["diffCount"], axis=1).values
#     plt.plot(x, y,"--",label=item)
# plt.xticks(fontsize=5)
# plt.yticks(fontsize=10)
# plt.xlabel("version", fontsize=10)
# plt.ylabel("times", fontsize=10)
# plt.title("Stablity for Versions")
# plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)
# plt.savefig("pictures/"+"stability_version.png")
# plt.show()


print(result["kvm"].sort_values(by=["subCount"],ascending=False)["patchName"].tolist())