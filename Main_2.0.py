import sys


def check_for_zero(key_value):
    pass


Standard_Map_Dict = {
    # 1001
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
    "Unique_Device_ID": 4,  # This is not always present
    "Account_Number": 0,  # Variable Length
    "Field_Sep_Track2": 1,
    "Exp_Date_Track2:": 4,
    "Disc_Data_Track2": 995,  # Variable_Length
    "Card_Use_Type": 1,  # Adding these to standard map to reduce replication
    "Total_Amount": 7,  # Adding these to standard map to reduce replication
}

Standard_Map_No_Unique_Dict = {
    # 1000
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
    "Account_Number": 0,  # Variable Length
    "Field_Sep_Track2": 1,
    "Exp_Date_Track2:": 4,
    "Disc_Data_Track2": 0,  # Variable_Length
    "Card_Use_Type": 1,  # Adding these to standard map to reduce replication
    "Total_Amount": 7,  # Adding these to standard map to reduce replication
}

Terminal_Diagnostics_Dict = {
    # 999
    "Number_Dial_Attempts": 1,
    "Terminal_Reason_Code": 2,
    "Host_Dialed": 1,
}

Terminal_Diagnostics_Plus_Dict = {
    # 998
    "Number_Dial_Attempts": 1,
    "Terminal_Reason_Code": 2,
    "Host_Dialed": 1,
    "Folio_Area_Tag": 2,
    "Purchase_ID_Format_Code": 1,
    "Reserved_2": 39,
    "Field_Separator_2": 1,
    "AVS_Area_Tag": 2,
    "AVS_Information": 0,
    "Field_Separator_3": 1,
    "Variable_Data_Area_Tag": 2,
}

Discretionary_Data_Dict = {
    # 997
    "Client_Discretionary_Data": 0,
    "Field_Separator": 1,
    "Field_Separator_Holder": 1,
}

Addendum_Tag_Data_Dict = {
    # 996
    "Field_Separator_2": 1,
    "Addendum_Data_Length": 4,
    "Number_Tag_IDs": 2,
    "Tag_ID": 3,
    "Tag_Data_Length": 4,
    "Tag_Data": 0,
    "Field_Separator_Holder_2": 1,
}

z01_Request_Field = {
    "01_C2": {
        "Standard_Map_No_Unique": 1000,
        "Currency_Code": 3,
        # Specific Information
        "Terminal_Type": 1,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Term_Reference_Number": 12,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "01_D3": {
        "Standard_Map_Dict": 1001,
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "01_D4": {
        "Standard_Map_Dict": 1001,
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Terminal_Type": 1,
        "PoS_Data_Codes": 12,
        "Authorization_Response_Code": 2,
        "Reserved": 20,
        "Addendum_Presence_Ind": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "03_C1": {
        "Standard_Map_Dict": 1001,
        "Currency_Code": 3,
        "Terminal_Type": 1,
        "Authorization_Number": 6,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "03_C2": {
        "Standard_Map_No_Unique": 1000,
        "Currency_Code": 3,
        # Specific Information
        "Authorization_Number": 6,
        "Terminal_Type": 1,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Retrieval_Ref_Num": 12,
        "Term_Reference_Number": 12,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "03_D0": {
        "Standard_Map_Dict": 1001,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Reserved": 8,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "B205": {
        # "Standard_Map_Dict": 1001,
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
        "Unique_Device_ID": 4,  # This is not always present
        "Account_Number": 0,  # Variable Length
        "Field_Sep_Track2": 1,
        "Exp_Date_Track2:": 4,
        "Disc_Data_Track2": 0,  # Variable_Length
        "Card_Use_Type": 1,  # Adding these to standard map to reduce replication
        "Total_Amount": 7,  # Adding these to standard map to reduce replication
        "CVV2_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Filler": 1,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Authorisation_Response_Code": 2,
        "Reserved": 4,
        "Goods_Sold": 1,
        "Reserved_2": 33,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        # "Terminal_Diagnostics": 999,
        "Number_Dial_Attempts": 1,
        "Terminal_Reason_Code": 2,
        "Host_Dialed": 1,
        # End of Term Diagnostics
        "Reserved_3": 19,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,  # Variable Length
        "Field Separator": 1,
        "Variable_Data_Area_Tag": 2,
        # Client Disc Data
        # "Discretionary_Data": 997,
        "Client_Discretionary_Data": 0,
        "Field_Separator": 1,
        "Field_Separator_Holder": 1,
        # Addendum_Tag_Data
        # "Addendum_Tag_Data": 996,
        "Field_Separator_2": 1,
        "Addendum_Data_Length": 4,
        "Number_Tag_IDs": 2,
        "Tag_ID": 3,
        "Tag_Data_Length": 4,
        "Tag_Data": 0,
        "Field_Separator_Holder_2": 1,
    },
    "05_F0": {
        "Standard_Map_Dict": 1001,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Filler": 1,
        "Good_Sold": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # End of Terminal Diagnostics
        "Folio_Area_Tag": 2,
        "Purch_ID_Format_Code": 1,
        "Reserved": 26,
        "Field_Separator": 1,
        "Reserved_2": 18,
        "Field_Separator_2": 1,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,  # Variable Length
        "Field Separator": 1,
        "Variable_Data_Area_Tag": 2,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_F2": {
        "Standard_Map_Dict": 1001,
        "CVV2_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Filler": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # End of Terminal Diagnostics
        "Folio_Area_Tag": 2,
        "Purch_ID_Format_Code": 1,
        "Reserved": 26,
        "Field_Separator": 1,
        "Reserved_2": 18,
        "Field_Separator_2": 1,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,  # Variable Length
        "Field Separator": 1,
        "Variable_Data_Area_Tag": 2,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_G2": {
        "Standard_Map_Dict": 1001,
        "Tax_Amount": 6,
        "Customer_Code": 25,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Authorisation_Response_Code": 2,
        "Reserved": 4,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Reserved_2": 32,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "05_NT": {
        "Standard_Map_Dict": 1001,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Reserved": 2,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_NO": {
        "Standard_Map_Dict": 1001,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_N2": {
        "Standard_Map_Dict": 1001,
        "Credit_Plan": 5,
        "Offered_Down_Payment": 7,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_N9": {
        "Standard_Map_Dict": 1001,
        "Card_Type": 4,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_P0": {
        "Standard_Map_Dict": 1001,
        "Tax_Amount": 6,
        "Customer_Code": 25,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_P5": {
        "Standard_Map_Dict": 1001,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_P6": {
        "Standard_Map_Dict": 1001,
        # This map appears identical to the P5...?
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_P7": {
        "Standard_Map_Dict": 1001,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "PO_Number": 15,
        "Business_Date": 6,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "05_P8": {
        "Standard_Map_Dict": 1001,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_Set": 2,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        "Authorisation_Response_Code": 2,
        "Settlement_Indicator": 1,
        "Reserved": 17,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "05_W7": {
        "Standard_Map_Dict": 1001,
        "Terminal_Type": 1,
        "Fuel_Service_Type": 2,
        "Prompt_Data": 43,
        "Vehicle_Card_Number": 5,
        "Addendum_Presence_Indicator": 1,
        "Available Products": 1,
        "Reserved": 1,
        "Unit_Measure": 1,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Unit_Measure_2": 1,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Unit_Measure_3": 1,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Unit_Measure_4": 1,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "11_B2": {
        "Standard_Map_Dict": 1001,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobil_Device_Indicator": 1,
        "Reserved": 66,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "11_E3": {
        "Standard_Map_Dict": 1001,
        "Currency_Code": 3,
        "EBT_Type": 2,
        "Terminal_Type": 1,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Voucher_Number": 15,
        "Reserved": 10,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "11_G2": {
        "Standard_Map_Dict": 1001,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Tax_Code": 6,
        "Customer_Code": 25,
        "Surcharge_Amount": 6,
        "PoS_Data_Code": 12,
        "Mobile_Device_Indicator": 1,
        "Terminal_Type": 1,
        "Reserved": 65,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "11_N8": {
        "Standard_Map_Dict": 1001,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "11_P0": {
        "Standard_Map_Dict": 1001,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Tax_Amount": 6,
        "Customer_Code": 25,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "11_P5": {
        "Standard_Map_Dict": 1001,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "11_P6": {
        "Standard_Map_Dict": 1001,
        # Again its the same as P5..?
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "11_P7": {
        "Standard_Map_Dict": 1001,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "PO_Number": 15,
        "Date": 6,
        "Invoice_Total": 12,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "11_P8": {
        "Standard_Map_Dict": 1001,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_Set": 2,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Reserved": 1,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        "Reserved_2": 20,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "11_W7": {
        "Standard_Map_Dict": 1001,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Fuel_Service_Type": 2,
        "Prompt_Data": 43,
        "Authorization_Amount": 7,
        "Purchase_Device_Seq_Number": 5,
        "Addendum_Presence_Indicator": 1,
        "Reserved": 2,
        "Unit_Measure": 1,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Unit_Measure_2": 1,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Unit_Measure_3": 1,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Unit_Measure_4": 1,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "13_B2": {
        "Standard_Map_Dict": 1001,
        "CVV2_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Purchase_Type": 1,
        "Terminal_Type": 1,
        "Cash_Over_Amount": 6,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Goods_Sold": 1,
        "Reserved": 3,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,
        "Field_Separator": 1,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "13_C2": {
        "Standard_Map_No_Unique": 1000,
        "Currency_Code": 3,
        # Specific Information
        "Terminal_Type": 1,
        "Sale_Type": 1,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Usage_Code": 1,
        "Terminal_Reference_Number": 12,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_D3": {
        "Standard_Map_Dict": 1001,
        # Same as 01 version..?
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_D4": {
        "Standard_Map_Dict": 1001,
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Terminal_Type": 1,
        "PoS_Data_Codes": 12,
        "Reserved": 21,
        "Addendum_Presence_Ind": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "13_E3": {
        "Standard_Map_Dict": 1001,
        "Currency_Code": 3,
        "EBT_Type": 2,
        "Terminal_Type": 1,
        "Purchase_Type": 1,
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Reserved": 25,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_F0": {
        "Standard_Map_Dict": 1001,
        "Mail_Indicator": 1,
        "Terminal_Type": 1,
        "Reserved": 2,
        # Term Diagnostics Plus
        "Terminal_Diagnostics_Plus": 0,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_F2": {
        "Standard_Map_Dict": 1001,
        "CVV2_Presence_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Purchase_Type": 1,
        "Terminal_Type": 1,
        "Filler": 1,
        # Term Diagnostics Plus
        "Terminal_Diagnostics_Plus": 0,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_G2": {
        "Standard_Map_Dict": 1001,
        "Tax_Amount": 6,
        "Customer_Code": 25,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Reserved": 65,
        "Addendum_Presence_indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "13_N0": {
        "Standard_Map_Dict": 1001,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_N2": {
        "Standard_Map_Dict": 1001,
        "Credit_Plan": 5,
        "Offered_Down_Payment": 7,
        "Product_Code_1": 4,
        "Product_Code_2": 4,
        "Product_Code_3": 4,
        "Product_Code_4": 4,
        "Product_Code_5": 4,
        "Unused": 11,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_P0": {
        "Standard_Map_Dict": 1001,
        "Tax_Code": 6,
        "Customer_Code": 25,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_P5": {
        "Standard_Map_Dict": 1001,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_P6": {
        "Standard_Map_Dict": 1001,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_P7": {
        "Standard_Map_Dict": 1001,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "PO_Number": 15,
        "Business_Date": 6,
        "Invoice_Total": 12,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "13_P8": {
        "Standard_Map_Dict": 1001,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_Set": 2,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        "Reserved": 20,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "13_W7": {
        "Standard_Map_Dict": 1001,
        "Terminal_Type": 1,
        "Fuel_Service_Type": 2,
        "Prompt_Data": 43,
        "Purchase_Device_Seq_Number": 5,
        "Addendum_Presence_Indicator": 1,
        "Reserved": 2,
        "Unit_Measure": 1,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Unit_Measure_2": 1,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Unit_Measure_3": 1,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Unit_Measure_4": 1,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "30_B2": {
        "Standard_Map_Dict": 1001,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Reserved": 1,
        "Reversal_Reason": 1,
        "Reserved_2": 40,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": 996,
    },
    "30_C2": {
        "Standard_Map_No_Unique": 1000,
        "Currency_Code": 3,
        # Specific Information
        "Terminal_Type": 1,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Term_Reference_Number": 12,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
    "30_??": {
        "Standard_Map_Dict": 1001,
        "Currency_Code": 3,
        "EBT_Type": 2,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Reserved": 10,
        # Term Diagnostics
        "Terminal_Diagnostics": 999,
        # Client Disc Data
        "Discretionary_Data": 997,
    },
}

# Entry point, takes multi-line input that needs formatting
print("Enter string, press 'ctrl+d' when done to input")
user_Input = str(sys.stdin.readlines())  # Reads multi-line string input and assigns to variable
print(user_Input)
print("~-~-~-~-~-~-~")

# Turns input into list of strings
user_Input = user_Input.split(",")
print(user_Input)

# Generic formatting. Ends by combining the list of strings into one string, with 1 space separator
user_Input_Combined = ''
for user_Input_String in user_Input:
    user_Input_String = user_Input_String.partition("INF:")[2]
    user_Input_String = user_Input_String.partition("\\")[0]
    user_Input_String = user_Input_String.replace("'", "")
    user_Input_String = user_Input_String.replace("]", "")
    user_Input_String = user_Input_String.replace("1E", "=")
    user_Input_String = user_Input_String.replace("1C", "=")
    print(user_Input_String)
    # user_Input_Combined = "".join(user_Input_String)
    user_Input_Combined += user_Input_String
    user_Input_Combined = user_Input_Combined.replace("      ", " ")
    user_Input_Combined = user_Input_Combined.replace("  ", " ")
    user_Input_Combined = user_Input_Combined.replace("   ", " ")

# Now that the data is formatted, it breaks the string into single 'byte' strings in a list
user_Input_List = user_Input_Combined.split(" ")
user_Input_List = user_Input_List[1:]  # Have to remove an awkward starting ' '
print(user_Input_List)

# Pulls the map type needed from the fully formatted list of single byte strings
request_format_code = "".join(user_Input_List[10:12])
transaction_type = "".join(user_Input_List[12:14])
map_selection = request_format_code + transaction_type


# Pass map_selection to auto determine which map type to parse
# Sorts data by Key:Value in specified sub-dictionary from the use_map and cuts out string values by Value in dict
def map_maker(dictionary):
    use_map = z01_Request_Field
    for x, y in use_map[dictionary].items():
        global user_Input_List
        start_index = 0
        end_index = 0
        end_index += y
        try:
            field_sep_keys = ["Account_Number", "AVS_Information", "Client_Discretionary_Data"]
            if x in field_sep_keys:  # Need to create 'if x == list of items that track field seps'
                end_index = user_Input_List.index("=")
                start_index = user_Input_List.index("=")
            elif x == "Disc_Data_Track2":
                end_index = user_Input_List.index(["C"])  # This needs to be modified to find multiple 'letters'
                start_index = user_Input_List.index("C")  # The 'letter' can change based on card type.
            elif x == "Tag_Data":
                tag_data_parse = "".join(user_Input_List[:user_Input_List.index("=")])
                print("Tag_Data_Parse: " + tag_data_parse)
                continue
        except ValueError:
            pass
        map_data = "".join(user_Input_List[:end_index:1])
        start_index += y
        user_Input_List = user_Input_List[start_index:]
        print(x + ": " + map_data)


# MAIN
map_maker(map_selection)
