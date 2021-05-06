def getParcelSize():
    stringParcelDim = input("Please enter parcel dimensions").split()
    parcelDimTotal = sum(map(int, stringParcelDim))

    if parcelDimTotal < 10:
        result = ("Small Parcel: $3. Total Cost $3")
    elif parcelDimTotal < 50 and parcelDimTotal > 10:
        result = ("Medium Parcel: $8. Total Cost $8")
    elif parcelDimTotal < 100 and parcelDimTotal > 50:
        result = ("Large Parcel: $15. Total Cost $15")
    else:
        result = ("Extra Large Parcel: $25. Total Cost $25")
    return result
getParcelSize()