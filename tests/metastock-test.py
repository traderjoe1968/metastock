import os
import metastock as ms

rootPath = r"D:\Trading\Data\Futures"

if __name__ == "__main__":

    d = []
    classPath = os.path.join(rootPath, "Continuous Contracts")
    for root, dirs, files in os.walk(classPath):
        d.extend(dirs)
    # print(d)

    contractPath = os.path.join(
        os.path.join(rootPath, "Continuous Contracts"), "Back Adjusted"
    )
    msObj = ms.MSDirectory(contractPath)
    # print(msObj)
    d = []
    for item in msObj:
        d.append(item.name)
    # print(d)
    msObj = ms.MSDataFrame(contractPath)
    symData = msObj.get("ES___CCB")
    print()
    #print(f"Name:{symData.name},Symbol:{symData.symbol}")
    print(symData.tail(5))