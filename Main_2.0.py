import sys

z01_Request_Fields = {
    "Standard_Map_Data": {
        "Company_Identifier": 4,
        "Terminal_Class_ID": 1,
        "Terminal_Format_Level": 2,
        "Multiple_Inquiry_Flag": 1,
        "Response_Format_Code": 2,
        "Request_Format_Code": 2,
        "Transaction_Type": 2,
        "Sequence_Number": 6,
        "Date": 6,
        "Time": 4,
        "Terminal_Location_ID": 15,  # Named Terminal_ID in spec's map info
        "Company_ID": 4,
        "Unique_Device_ID": 4,
        "Account_Number": 0,  # Variable Length
        "Field_Sep_Track2": 1,
        "Exp_Date_Track2:": 4,
        "Disc_Data_Track2": 0,  # Variable_Length
        "Card_Use_Type": 1,
        "Total_Amount": 7,
        "Currency_Code": 3,
        "Terminal_Type": 1,
        "Authorization_Number:": 6,
    },
    "Detail_Information": {
        # "Track_1": 76,  # 76 is the max value
        "Track_2": 37,  # 37 is the max value
        "Card_Use_Type": 1,
        "Total_Amount": 7,
        "Credit_Plan": 5,
        "Authorization_Number": 6,
        "Authorization_Type": 1,
        "Surcharge_Amount": 6,
        "Offered_Down_Payment": 7,
        "Tax_Amount": 6,
        "Chip_Condition_Code": 1,
        "PO_number": 15,
        "CVV2_Presence_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Settlement_Indicator": 1,
        "Filler": 1,
        "KSN": [0, 16, 20],
        "Encrypted_Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Terminal_Type": 1,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Authorisation_Response_Code": 2,
        "Reserved": [1, 4, 17, 20, 66],
        "Addendum_Presence_Indicator": 1,
        "Currency_Code": 3,
        "Goods_Sold": 1,
        "Card_Type": 4,
        "Customer_Code": 25,
        "Odometer": 6,
        "Driver_Number": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Prompt_Data": 43,
        "Purchase_Device_Seq_Num": 5,
        "Avail_Prod_Capable_Ind": 1,
        "Product_Code_Set": 2,
        "Unit_Measure_1": 1,
        "Product_Code_1": [2, 3],
        "Quantity_1": 7,
        "Amount_1": 7,
        "Unit_Measure_2": 1,
        "Product_Code_2": [2, 3],
        "Quantity_2": 7,
        "Amount_2": 7,
        "Unit_Measure_3": 1,
        "Product_Code_3": [2, 3],
        "Quantity_3": 7,
        "Amount_3": 7,
        "Unit_Measure_4": 1,
        "Product_Code_4": [2, 3],
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": [2, 3],
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": [2, 3],
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,

    },
    "Specific_Information": {
        "Terminal Type": 1,
        "Authorization_Number": 6,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Terminal_Reference_Number": 12,
        "Retrieval_Ref_Num": 12,
        "Term_Ref_Num": 12
    },
    "Terminal_Diagnostics": {
        "Number_Dial_Attempts": 1,
        "Terminal_Reason_Code": 2,
        "Host_Dialed": 1,
    },
    "End_Terminal_Diagnostics": {
        "Reserved": [18, 19, 26],
        "Folio_Area_Tag": 2,
        "Purchase_ID_Format_Code": 1,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,  # Variable Length
        "Field_Separator": 1,
        "Variable_Data_Area_Tag": 2,

    },
    "Client_Discretionary_Data_Dict": {
        "Client_Discretionary_Data": 0,  # Variable Length Data
        "Field_Separator": 1,
        "Field_Separator_Holder": 1,
    },
    "Addendum_Data_Length": {
        "Field_Separator": 1,
        "Addendum_Data_Length": 4,
        "Number Tag_IDs": 2,
        "Tag ID": 3,
        "Tag_Data_Length": 4,
        "Tag_Data": 0,
        "Field_Separator_Holder": 0
    },
    "Disc_Data_Capture_Fields": {
        "Authorization_Disc_Data": 0,  # Variable Length
        "Capture_Field_Identifier": 1,
        "Terminal_Type": 1,
        "Capture_Sequence_Number": 6,
        "Capture_Total_Amount": 6,
        "Capture_Disc_Data": 0,  # Variable Length
        "Field_Separator": 1,
        "Field_Separator_Holder": 1
    },


}

print("Enter string, press 'ctrl+d' when done to input")
user_Input = str(sys.stdin.readlines())  # Reads multi-line string input and assigns to variable
print(user_Input)
print("~-~-~-~-~-~-~")

user_Input = user_Input.split(",")
print(user_Input)

user_Input_Combined = ''
for user_Input_String in user_Input:
    user_Input_String = user_Input_String.partition("INF:      ")[2]
    user_Input_String = user_Input_String.partition("\\n'")[0]
    user_Input_String = user_Input_String.replace("'", "")
    user_Input_String = user_Input_String.replace("]", "")
    user_Input_Combined += user_Input_String + " "

user_Input_Combined = user_Input_Combined.replace("  ", " ")
user_Input_List = user_Input_Combined.split(" ")
print(user_Input_List)
