def getParcelSize():
    stringParcelDim = input("Please enter parcel dimensions").split()
    parcelDimTotal = sum(map(int, stringParcelDim))

    if parcelDimTotal < 10:
        print("Small Parcel: $3. Total Cost $3")
    elif parcelDimTotal < 50 and parcelDimTotal > 10:
        print("Medium Parcel: $8. Total Cost $8")
    elif parcelDimTotal < 100 and parcelDimTotal > 50:
        print("Large Parcel: $15. Total Cost $15")
    else:
        print("Extra Large Parcel: $25. Total Cost $25")
getParcelSize()