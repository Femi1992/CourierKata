class Order:
    def __init__(self):
        self.orderTotal = 0
        self.parcelSize = ""

    def getParcelSize(self):
        stringParcelDim = input("Please enter parcel dimensions with spaces like so: 3 4 8: ").split()
        parcelDimTotal = sum(map(int, stringParcelDim))

        if parcelDimTotal < 10:
            result = "Small Parcel: $3. Total Cost $3"
            self.orderTotal += 3
            self.parcelSize = "Small Parcel"
        elif parcelDimTotal < 50 and parcelDimTotal > 10:
            result = "Medium Parcel: $8. Total Cost $8"
            self.orderTotal += 8
            self.parcelSize = "Medium Parcel"
        elif parcelDimTotal < 100 and parcelDimTotal > 50:
            result = "Large Parcel: $15. Total Cost $15"
            self.orderTotal += 15
            self.parcelSize = "Large Parcel"
        else:
            result = "Extra Large Parcel: $25. Total Cost $25"
            self.orderTotal += 25
            self.parcelSize = "Extra Large Parcel"
        return result

    def getParcelWeight(self):
        parcelWeight = int(input("Please enter the weight of the parcel in KG: "))
        if self.parcelSize == "Small Parcel" and parcelWeight > 1:
            overWeight = parcelWeight - 1
            overWeight = overWeight * 2
            self.orderTotal += overWeight
        elif self.parcelSize == "Medium Parcel" and parcelWeight > 3:
            overWeight = parcelWeight - 3
            overWeight = overWeight * 2
            self.orderTotal += overWeight
        elif self.parcelSize == "Large Parcel" and parcelWeight > 6:
            overWeight = parcelWeight - 6
            overWeight = overWeight * 2
            self.orderTotal += overWeight
        elif self.parcelSize == "Extra Large Parcel" and parcelWeight > 10:
            overWeight = parcelWeight - 10
            overWeight = overWeight * 2
            self.orderTotal += overWeight
        elif parcelWeight > 50:
            overWeight = parcelWeight - 50
            overWeight = overWeight * 1
            self.orderTotal += overWeight

    def speedyShipping(self):
        addSpeedShip = input("Would you like speeding shipping for your order? Please state yes or no: ")
        if addSpeedShip == "yes":
            self.orderTotal = self.orderTotal * 2

if __name__ == '__main__':
     order = Order()
     order.getParcelSize()
     #order.speedyShipping()