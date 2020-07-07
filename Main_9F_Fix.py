import sys


def parse_cutter(string_cut):
    temp_string = ""
    global formatted_string  # Makes the full_string string avail. to the function
    for char in formatted_string[0:string_cut:1]:  # Loops through the specified range set by the value passed to the
        # function
        temp_string = str(temp_string) + str(char)  # Creates the string snippet
        formatted_string = formatted_string.replace(char, "",
                                                    1)  # Cuts the original string after passing the needed value
    return temp_string
    # return formatted_string


def company_ident(length):
    company_identifier = parse_cutter(length)
    print("Company Identifier: " + str(company_identifier))


def term_class(length):
    term_class_id = parse_cutter(length)
    print("Terminal Class ID: " + term_class_id)


def term_format_level(length):
    term_format_level = parse_cutter(length)
    print("Terminal Format Level: " + term_format_level)


def multi_inq_flag(length):
    multi_inq_flag = parse_cutter(length)
    print("multi_inq_flag: " + multi_inq_flag)


def resp_form_code(length):
    resp_form_code = parse_cutter(length)
    print("resp_form_code: " + resp_form_code)
    return resp_form_code


def req_form_code(length):
    req_form_code = parse_cutter(length)
    print("req_form_code: " + req_form_code)
    return req_form_code


def tran_type(length):
    tran_type = parse_cutter(length)
    print("tran_type: " + tran_type)
    return tran_type


def seq_num(length):
    seq_num = parse_cutter(length)
    print("seq_num: " + seq_num)


def date(length):
    date = parse_cutter(length)
    print("date: " + date)


def time(length):
    time = parse_cutter(length)
    print("Time: " + time)


def term_loc_id(length):
    term_loc_id = parse_cutter(length)
    print("term_loc_id: " + term_loc_id)


def comp_id(length):
    comp_id = parse_cutter(length)
    print("comp_id: " + comp_id)


def uniq_dev_id(length):
    uniq_dev_id = parse_cutter(length)
    print("uniq_dev_id: " + uniq_dev_id)


### Track Data Section Definition ###

#def track_2(length):
    #track_2 = parse_cutter(length)
    #print("track_2: " + track_2)

def track_2():  # Huge bug here when Card Use type is not C
    global formatted_string
    track_2 = formatted_string[:formatted_string.find("C")]
    print("track_2: " + track_2)
    formatted_string = formatted_string[formatted_string.find("C"):]

#def misc_data(length):
    #misc_data = parse_cutter(length)
    #print("misc_data: " + misc_data)


### Request Type Definition ###

def card_use_type(length):
    card_use_type = parse_cutter(length)
    print("card_use_type: " + card_use_type)


def tot_amnt(length):
    tot_amnt = parse_cutter(length)
    print("tot_amnt: " + tot_amnt)


def term_type(length):
    term_type = parse_cutter(length)
    print("term_type: " + term_type)


def odometer(length):
    odometer = parse_cutter(length)
    print("odometer: " + odometer)


def driver_num(length):
    driver_num = parse_cutter(length)
    print("driver_num: " + driver_num)


def po_num(length):
    po_num = parse_cutter(length)
    print("po_num: " + po_num)


def bus_date(length):
    bus_date = parse_cutter(length)
    print("bus_date: " + bus_date)


def inv_tot(length):
    inv_tot = parse_cutter(length)
    print("inv_tot: " + inv_tot)


def veh_number(length):
    veh_number = parse_cutter(length)
    print("veh_number: " + veh_number)


def fuel_measure(length):
    fuel_measure = parse_cutter(length)
    print("fuel_measure: " + fuel_measure)


def fuel_serv_type(length):
    fuel_serv_type = parse_cutter(length)
    print("fuel_serv_type: " + fuel_serv_type)


def prod_code_1(length):
    prod_code_1 = parse_cutter(length)
    print("prod_code_1: " + prod_code_1)


def quant_1(length):
    quant_1 = parse_cutter(length)
    print("quant_1: " + quant_1)


def amt_1(length):
    amt_1 = parse_cutter(length)
    print("amt_1: " + amt_1)


def prod_code_2(length):
    prod_code_2 = parse_cutter(length)
    print("prod_code_2: " + prod_code_2)


def quant_2(length):
    quant_2 = parse_cutter(length)
    print("quant_2: " + quant_2)


def amt_2(length):
    amt_2 = parse_cutter(length)
    print("amt_2: " + amt_2)


def prod_code_3(length):
    prod_code_3 = parse_cutter(length)
    print("prod_code_3: " + prod_code_3)


def quant_3(length):
    quant_3 = parse_cutter(length)
    print("quant_3: " + quant_3)


def amt_3(length):
    amt_3 = parse_cutter(length)
    print("amt_3: " + amt_3)


def prod_code_4(length):
    prod_code_4 = parse_cutter(length)
    print("prod_code_4: " + prod_code_4)


def quant_4(length):
    quant_4 = parse_cutter(length)
    print("quant_4: " + quant_4)


def amt_4(length):
    amt_4 = parse_cutter(length)
    print("amt_4: " + amt_4)


def prod_code_5(length):
    prod_code_5 = parse_cutter(length)
    print("prod_code_5: " + prod_code_5)


def quant_5(length):
    quant_5 = parse_cutter(length)
    print("quant_5: " + quant_5)


def amt_5(length):
    amt_5 = parse_cutter(length)
    print("amt_5: " + amt_5)


def prod_code_6(length):
    prod_code_6 = parse_cutter(length)
    print("prod_code_6: " + prod_code_6)


def quant_6(length):
    quant_6 = parse_cutter(length)
    print("quant_6: " + quant_6)


def amt_6(length):
    amt_6 = parse_cutter(length)
    print("amt_6: " + amt_6)


def sale_tax(length):
    sale_tax = parse_cutter(length)
    print("sale_tax: " + sale_tax)


def discount(length):
    discount = parse_cutter(length)
    print("discount: " + discount)


def num_dial_attempt(length):
    num_dial_attempt = parse_cutter(length)
    print("num_dial_attempt: " + num_dial_attempt)


def term_reason_code(length):
    term_reason_code = parse_cutter(length)
    print("term_reason_code: " + term_reason_code)


def host_dialed(length):
    host_dialed = parse_cutter(length)
    print("host_dialed: " + host_dialed)


# def disc_data()(length):
#    disc_data() = parse_cutter(length)
#    print("disc_data(): " + disc_data())


def disc_data():
    global formatted_string
    disc_data_str = formatted_string.partition("_")[0]
    if disc_data_str == "":
        print("disc_data:None")
    else:
        #print("disc_data: " + disc_data_str) #Night have to rework for URCC/GRMK setup
        n = 18 # Value that determines how many chars to split by
        out = [(disc_data_str[i:i + n]) for i in range(0, len(disc_data_str), n)] # No idea how this works. Splits string ever nth character
        for x in out: # Prints each list item nicely
            print("disc_data: " + x)

    formatted_string = formatted_string[len(disc_data_str):]


def field_sep(length):
    field_sep = parse_cutter(length)
    print("field_sep: " + field_sep)


def ksn(length):
    ksn = parse_cutter(length)
    print("KSN: " + ksn)


def pin_block(length):
    pin_block = parse_cutter(length)
    print("pin_block: " + pin_block)


def cash_back(length):
    cash_back = parse_cutter(length)
    print("cash_back: " + cash_back)


def conv_fee_amt(length):
    conv_fee_amt = parse_cutter(length)
    print("conv_fee_amt: " + conv_fee_amt)


def alt_term_type(length):
    alt_term_type = parse_cutter(length)
    print("alt_term_type: " + alt_term_type)


#def POS_data_code(length):  # Duplicate function
    #POS_data_code = parse_cutter(length)
    #print("POS_data_code: " + POS_data_code)



def auth_resp_code(length):
    auth_resp_code = parse_cutter(length)
    print("auth_resp_code: " + auth_resp_code)


def reserved(length):
    reserved = parse_cutter(length)
    print("reserved: " + reserved)


def adden_pres_ind(length):
    adden_pres_ind = parse_cutter(length)
    print("adden_pres_ind: " + adden_pres_ind)


def adden_data_length(length):
    adden_data_length = parse_cutter(length)
    print("adden_data_length: " + adden_data_length)


def num_tag_id(length):
    num_tag_id = parse_cutter(length)
    print("num_tag_id: " + num_tag_id)


def tag_id(length):
    tag_id = parse_cutter(length)
    print("tag_id: " + tag_id)


def tag_data_length(length):
    tag_data_length = parse_cutter(length)
    tag_length = tag_data_length
    print("tag_data_length: " + tag_data_length)




def tag_data():
    #global formatted_string

    tag_data = parse_cutter((len(formatted_string)-2)) # -2 accounts for the ending field sep values. Creates tag data by taking parse cutter value from the remaining length of the formatted string
    pre_tag_data = tag_data[:(tag_data.find("9F"))]
    post_tag_data = tag_data[(tag_data.find("9F")):]
    print("Pre_EMV_Tag_Data: "+ pre_tag_data)
    #print(post_tag_data)
    #print(post_tag_data.split("9F"))
    for tag in (post_tag_data.split("9F")[1:]): # Indexed to remove a blank entry. Splits 9F tags into lists
        print("EMV Tag: 9F" + tag)



def cur_code(length):
    cur_code = parse_cutter(length)
    print("cur_code: " + cur_code)


def card_type(length):
    card_type = parse_cutter(length)
    print("card_type: " + card_type)


def emply_id(length):
    emply_id = parse_cutter(length)
    print("emply_id: " + emply_id)


def shift_num(length):
    shift_num = parse_cutter(length)
    print("shift_num: " + shift_num)


def control_num(length):
    control_num = parse_cutter(length)
    print("control_num: " + control_num)


def access_code(length):
    access_code = parse_cutter(length)
    print("access_code: " + access_code)


def term_ref_num(length):
    term_ref_num = parse_cutter(length)
    print("term_ref_num: " + term_ref_num)


def cid_ind(length):
    cid_ind = parse_cutter(length)
    print("cid_ind: " + cid_ind)


def cid(length):
    cid = parse_cutter(length)
    print("cid: " + cid)


def moto_ind(length):
    moto_ind = parse_cutter(length)
    print("moto_ind: " + moto_ind)


def settle_ind(length):
    settle_ind = parse_cutter(length)
    print("settle_ind: " + settle_ind)


def pos_data_code(length):
    pos_data_code = parse_cutter(length)
    print("pos_data_code: " + pos_data_code + " See Table F-1 for a breakdown")


def mobile_dev_ind(length):
    mobile_dev_ind = parse_cutter(length)
    print("mobile_dev_ind: " + mobile_dev_ind)


def chip_cond_code(length):
    chip_cond_code = parse_cutter(length)
    print("chip_cond_code: " + chip_cond_code)


def auth_resp_code(length):
    auth_resp_code = parse_cutter(length)
    print("auth_resp_code: " + auth_resp_code)


def goods_sold(length):
    goods_sold = parse_cutter(length)
    print("goods_sold: " + goods_sold)


def avs_area_tag(length):
    avs_area_tag = parse_cutter(length)
    print("avs_area_tag: " + avs_area_tag)


# def avs_info(length):
#    avs_info = parse_cutter(length)
#    print("avs_info: " + avs_info)


def avs_info():
    global formatted_string
    avs_info_str = formatted_string.partition("_")[0]
    if avs_info_str == "":
        print("AVS info:None")
    else:
        print("AVS_Info: " + avs_info_str)
    formatted_string = formatted_string[len(avs_info_str):]



def var_data_area_tag(length):
    var_data_area_tag = parse_cutter(length)
    print("var_data_area_tag: " + var_data_area_tag)


def cust_code(length):
    cust_code = parse_cutter(length)
    print("cust_code: " + cust_code)


def prod_code_set(length):
    prod_code_set = parse_cutter(length)
    print("prod_code_set: " + prod_code_set)


def auth_num(length):
    auth_num = parse_cutter(length)
    print("auth_num: " + auth_num)


def auth_type(length):
    auth_type = parse_cutter(length)
    print("auth_type: " + auth_type)


def surcharge(length):
    surcharge = parse_cutter(length)
    print("surcharge: " + surcharge)


def purchase_type(length):
    purchase_type = parse_cutter(length)
    print("purchase_type: " + purchase_type)


def cash_over_amt(length):
    cash_over_amt = parse_cutter(length)
    print("cash_over_amt: " + cash_over_amt)


def sale_type(length):
    sale_type = parse_cutter(length)
    print("sale_type: " + sale_type)


def use_code(length):
    use_code = parse_cutter(length)
    print("use_code: " + use_code)


def part_apprv_ind(length):
    part_apprv_ind = parse_cutter(length)
    print("part_apprv_ind: " + part_apprv_ind)


def term_id(length):
    term_id = parse_cutter(length)
    print("term_id: " + term_id)


def ret_ref_num(length):
    ret_ref_num = parse_cutter(length)
    print("ret_ref_num: " + ret_ref_num)


def key_serial_num(length):
    key_serial_num = parse_cutter(length)
    print("key_serial_num: " + key_serial_num)


def ebt_type(length):
    ebt_type = parse_cutter(length)
    print("key_serial_num: " + ebt_type)


def voucher_num(length):
    voucher_num = parse_cutter(length)
    print("voucher_num: " + voucher_num)


def p7_13():
    ### Map Type Data
    card_use_type(1)
    tot_amnt(7)
    term_type(1)
    odometer(6)
    driver_num(6)
    po_num(15)
    bus_date(6)
    inv_tot(12)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    ### Product data
    prod_code_1(3)
    quant_1(7)
    amt_1(7)
    prod_code_2(3)
    quant_2(7)
    amt_2(7)
    prod_code_3(3)
    quant_3(7)
    amt_3(7)
    prod_code_4(3)
    quant_4(7)
    amt_4(7)
    sale_tax(5)
    discount(5)
    ### Term Diagnostic
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    disc_data()  # Gotta solve this. Maybe cut string and just display all?
    field_sep(1)
    field_sep(1)
    print(formatted_string)


def d3_01():
    ### Map Type Data
    card_use_type(1)
    tot_amnt(7)
    ksn(16)
    pin_block(16)
    cash_back(6)
    conv_fee_amt(6)

    ### Term Diagnostic
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    disc_data()  # Disc Data is flexable. Maybe just print rest of string here.
    field_sep(1)
    field_sep(1)
    print(formatted_string)


def d4_01():
    ### Map Type Data
    card_use_type(1)
    tot_amnt(7)
    ksn(16)
    pin_block(16)
    cash_back(6)
    conv_fee_amt(6)
    alt_term_type(1)
    pos_data_code(12)
    auth_resp_code(2)
    reserved(20)
    adden_pres_ind(1)

    ### Term Diagnostic
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    disc_data()  # Disc Data is flexable. Maybe just print rest of string here.
    field_sep(1)
    field_sep(1)
    print(formatted_string)

    ### Addendum Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Variable length
    field_sep(1)


def c1_01():
    ### Map Type Data
    card_use_type(1)
    tot_amnt(7)
    cur_code(3)
    term_type(1)

    ### Term Diagnostic
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    disc_data()  # Disc Data is flexable. Maybe just print rest of string here.
    field_sep(1)
    field_sep(1)
    print(formatted_string)


def c2_01():
    ### Map Type Data
    comp_id(4)
    term_class(1)
    term_format_level(2)
    multi_inq_flag(1)
    resp_form_code(2)
    req_form_code(2)
    tran_type(2)
    seq_num(6)
    date(6)
    time(4)
    term_loc_id(15)
    comp_id(8)
    track_2(37)
    card_use_type(1)
    tot_amnt(7)
    cur_code(3)
    term_type(1)
    card_type(4)
    emply_id(8)
    shift_num(3)
    control_num(6)
    access_code(4)
    term_ref_num(12)

    ### Term Diagnostic
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    disc_data()  # Disc Data is flexable. Maybe just print rest of string here.
    field_sep(1)
    field_sep(1)
    print(formatted_string)


def b2_05():
    card_use_type(1)
    tot_amnt(7)
    cid_ind(1)
    cid(4)
    moto_ind(1)
    term_type(1)
    settle_ind(1)
    field_sep(1)
    pos_data_code(12)
    mobile_dev_ind(1)
    chip_cond_code(1)
    auth_resp_code(2)
    reserved(4)
    goods_sold(1)
    reserved(33)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    field_sep(19)
    avs_area_tag(2)
    avs_info()  # Variable Length
    field_sep(1)
    var_data_area_tag(2)
    # Discretionary Data
    disc_data()
    field_sep(2)
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Variable length
    field_sep(1)


def n0_05():
    card_use_type(1)
    tot_amnt(7)
    # term diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # disc data
    disc_data()  # Var length
    field_sep(2)


def p0_05():
    card_use_type(1)
    tot_amnt(7)
    sale_tax(6)
    cust_code(25)
    # term diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # disc data
    disc_data()  # Var length
    field_sep(2)


def p5_05():
    card_use_type(1)
    tot_amnt(7)
    term_type(1)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(5)
    discount(5)
    # term diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # disc data
    disc_data()  # Var length
    field_sep(2)


def p6_05():
    card_use_type(1)
    tot_amnt(7)
    term_type(1)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(5)
    discount(5)
    # term diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # disc data
    disc_data()  # Var length
    field_sep(2)


def p7_05():
    card_use_type(1)
    tot_amnt(7)
    term_type(1)
    odometer(6)
    driver_num(6)
    po_num(15)
    bus_date(6)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(3)
    quant_1(7)
    amt_1(7)
    prod_code_2(3)
    quant_2(7)
    amt_2(7)
    prod_code_3(3)
    quant_3(7)
    amt_3(7)
    prod_code_4(3)
    quant_4(7)
    amt_4(7)
    sale_tax(5)
    discount(5)
    # term diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # disc data
    disc_data()  # Var length
    field_sep(2)


def p8_05():
    card_use_type(1)
    tot_amnt(7)
    term_type(1)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_set(2)
    pos_data_code(12)
    mobile_dev_ind(1)
    chip_cond_code(1)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(5)
    discount(5)
    auth_resp_code(2)
    settle_ind(1)
    field_sep(17)
    adden_pres_ind(1)
    # term diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # disc data
    disc_data()  # Var length
    field_sep(2)
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var Length
    field_sep(1)


def b2_11():
    card_use_type(1)
    tot_amnt(7)
    auth_num(6)
    auth_type(1)
    term_type(1)
    surcharge(6)
    pos_data_code(12)
    mobile_dev_ind(1)
    reserved(66)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()
    field_sep(2)
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Variable length
    field_sep(1)


def p0_11():
    card_use_type(1)
    tot_amnt(7)
    auth_num(6)
    auth_type(1)
    sale_tax(6)
    cust_code(25)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()
    field_sep(2)


def p5_11():
    card_use_type(1)
    tot_amnt(7)
    auth_num(6)
    auth_type(1)
    term_type(1)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(6)
    discount(5)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p6_11():
    card_use_type(1)
    tot_amnt(7)
    auth_num(6)
    auth_type(1)
    term_type(1)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(6)
    discount(5)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p7_11():
    card_use_type(1)
    tot_amnt(7)
    auth_num(6)
    auth_type(1)
    term_type(1)
    odometer(6)
    driver_num(6)
    po_num(15)
    bus_date(6)
    inv_tot(12)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    sale_tax(6)
    discount(5)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p8_11():
    card_use_type(1)
    tot_amnt(7)
    auth_num(6)
    auth_type(1)
    term_type(1)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_set(2)
    surcharge(6)
    pos_data_code(12)
    mobile_dev_ind(1)
    field_sep(1)
    prod_code_1(3)
    quant_1(7)
    amt_1(7)
    prod_code_2(3)
    quant_2(7)
    amt_2(7)
    prod_code_3(3)
    quant_3(7)
    amt_3(7)
    prod_code_4(3)
    quant_4(7)
    amt_4(7)
    prod_code_5(3)
    quant_5(7)
    amt_5(7)
    prod_code_6(3)
    quant_6(7)
    amt_6(7)
    sale_tax(6)
    discount(5)
    field_sep(20)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)
    # Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var length
    field_sep(1)


def b2_13():
    card_use_type(1)
    tot_amnt(7)
    cid_ind(1)
    cid(4)
    moto_ind(1)
    purchase_type(1)
    term_type(1)
    cash_over_amt(6)
    surcharge(6)
    pos_data_code(12)
    mobile_dev_ind(1)
    chip_cond_code(1)
    goods_sold(1)
    reserved(3)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    avs_area_tag(2)
    avs_info()  # Var length
    field_sep(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(1)
    field_sep(1)
    # Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var length
    field_sep(1)


def c1_13():
    card_use_type(1)
    tot_amnt(7)
    cur_code(3)
    term_type(1)
    purchase_type(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def c2_13():
    company_ident(4)
    term_class(1)
    term_format_level(2)
    multi_inq_flag(1)
    resp_form_code(2)
    req_form_code(2)
    tran_type(2)
    seq_num(6)
    date(6)
    time(4)
    term_loc_id(15)
    comp_id(8)
    # Track 2
    track_2(37)
    card_use_type(1)
    tot_amnt(7)
    cur_code(3)
    # Special info
    term_type(1)
    sale_type(1)
    card_type(4)
    emply_id(8)
    shift_num(3)
    control_num(6)
    access_code(4)
    use_code(1)
    term_ref_num(12)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def d3_13():
    card_use_type(1)
    tot_amnt(7)
    ksn(16)
    pin_block(16)
    cash_back(6)
    conv_fee_amt(6)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def d4_13():
    card_use_type(1)
    tot_amnt(7)
    ksn(20)
    pin_block(16)
    cash_back(6)
    conv_fee_amt(6)
    term_type(1)
    pos_data_code(12)
    field_sep(21)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)
    # Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var Length
    field_sep(1)


def n0_13():
    card_use_type(1)
    tot_amnt(7)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p0_13():
    card_use_type(1)
    tot_amnt(7)
    sale_tax(6)
    cust_code(25)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p5_13():
    card_use_type(1)
    tot_amnt(7)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(6)
    discount(5)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p6_13():
    card_use_type(1)
    tot_amnt(7)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(6)
    discount(5)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p8_13():
    card_use_type(1)
    tot_amnt(7)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_set(2)
    surcharge(6)
    pos_data_code(12)
    mobile_dev_ind(1)
    chip_cond_code(1)
    prod_code_1(3)
    quant_1(7)
    amt_1(7)
    prod_code_2(3)
    quant_2(7)
    amt_2(7)
    prod_code_3(3)
    quant_3(7)
    amt_3(7)
    prod_code_4(3)
    quant_4(7)
    amt_4(7)
    #prod_code_5(3)
    #quant_5(7)
    #amt_5(7)
    #prod_code_6(3)
    #quant_6(7)
    #amt_6(7)
    sale_tax(5)
    discount(5)
    reserved(20)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)
    # Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var Length
    field_sep(1)


def b2_32():
    card_use_type(1)
    tot_amnt(7)
    tran_type(2)
    part_apprv_ind(1)
    cash_back(6)
    pos_data_code(12)
    mobile_dev_ind(1)
    reserved(40)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)
    # Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var Length
    field_sep(1)


def c2_32():
    comp_id(4)
    term_class(1)
    term_format_level(2)
    multi_inq_flag(1)
    resp_form_code(2)
    req_form_code(2)
    tran_type(2)
    seq_num(6)
    date(6)
    time(4)
    term_id(15)
    comp_id(8)
    # Track 2
    track_2(37)
    card_use_type(1)
    tot_amnt(7)
    cur_code(3)
    # Special Info
    term_type(1)
    card_type(4)
    emply_id(8)
    shift_num(3)
    control_num(6)
    access_code(4)
    ret_ref_num(12)
    term_ref_num(12)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def d4_32():
    card_use_type(1)
    tot_amnt(7)
    key_serial_num(20)
    pin_block(16)
    term_type(1)
    pos_data_code(12)
    reserved(20)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p3_32():
    card_use_type(1)
    tot_amnt(7)
    tran_type(2)
    part_apprv_ind(1)
    cash_back(6)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def n0_32():
    card_use_type(1)
    tot_amnt(7)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def b2_34():
    card_use_type(1)
    tot_amnt(7)
    surcharge(6)
    pos_data_code(12)
    reserved(1)
    chip_cond_code(1)
    reserved(25)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)
    # Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var Length
    field_sep(1)


def c2_34():
    comp_id(4)
    term_class(1)
    term_format_level(2)
    multi_inq_flag(1)
    resp_form_code(2)
    req_form_code(2)
    tran_type(2)
    seq_num(6)
    date(6)
    time(4)
    term_id(15)
    comp_id(8)
    # Track 2
    track_2(37)
    card_use_type(1)
    tot_amnt(7)
    cur_code(3)
    # Special Info
    term_type(1)
    sale_type(1)
    card_type(4)
    emply_id(8)
    shift_num(3)
    control_num(6)
    access_code(4)
    use_code(1)
    term_ref_num(12)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def d3_34():
    card_use_type(1)
    tot_amnt(7)
    ksn(16)
    pin_block(16)
    cash_back(6)
    conv_fee_amt(6)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def d4_34():
    card_use_type(1)
    tot_amnt(7)
    ksn(20)
    pin_block(16)
    cash_back(6)
    conv_fee_amt(6)
    term_type(1)
    pos_data_code(12)
    reserved(20)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)
    # Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var Length
    field_sep(1)


def e3_34():
    card_use_type(1)
    tot_amnt(7)
    cur_code(3)
    ebt_type(2)
    term_type(1)
    auth_num(6)
    ksn(16)
    pin_block(16)
    cash_back(6)
    conv_fee_amt(6)
    voucher_num(15)
    reserved(10)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def n0_34():
    card_use_type(1)
    tot_amnt(7)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p0_34():
    card_use_type(1)
    tot_amnt(7)
    sale_tax(6)
    cust_code(25)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p5_34():
    card_use_type(1)
    tot_amnt(7)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(6)
    discount(5)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p6_34():
    card_use_type(1)
    tot_amnt(7)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(6)
    discount(5)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p7_34():
    card_use_type(1)
    tot_amnt(7)
    term_type(1)
    odometer(6)
    driver_num(6)
    po_num(15)
    bus_date(6)
    inv_tot(12)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_1(2)
    surcharge(6)
    pos_data_code(12)
    mobile_dev_ind(1)
    chip_cond_code(1)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    sale_tax(6)
    discount(5)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)


def p8_34():
    card_use_type(1)
    tot_amnt(7)
    odometer(6)
    driver_num(6)
    control_num(4)
    veh_number(6)
    fuel_measure(1)
    fuel_serv_type(2)
    prod_code_set(2)
    surcharge(6)
    prod_code_1(2)
    quant_1(7)
    amt_1(7)
    prod_code_2(2)
    quant_2(7)
    amt_2(7)
    prod_code_3(2)
    quant_3(7)
    amt_3(7)
    prod_code_4(2)
    quant_4(7)
    amt_4(7)
    prod_code_5(2)
    quant_5(7)
    amt_5(7)
    prod_code_6(2)
    quant_6(7)
    amt_6(7)
    sale_tax(6)
    discount(5)
    pos_data_code(12)
    reserved(1)
    chip_cond_code(1)
    reserved(6)
    adden_pres_ind(1)
    # Term Diag
    num_dial_attempt(1)
    term_reason_code(2)
    host_dialed(1)
    # Discretionary Data
    disc_data()  # Var length
    field_sep(2)
    # Tag Data
    field_sep(1)
    adden_data_length(4)
    num_tag_id(2)
    tag_id(3)
    tag_data_length(4)
    tag_data()  # Var Length
    field_sep(1)


### Start of actual program ###

temp_string = ""
print("Enter string, press 'ctrl+d' when done to input")
user_input = str(sys.stdin.readlines())  # Reads multi-line string input and assigns to variable
print(user_input)
print("~-~-~-~-~-~-~")

# try:
user_input = user_input.split(",")  # Splits the one line list into smaller string segments
# except():


print(user_input)
print(type(user_input))

full_string = []
for x in user_input:  # Runs through each string segment to format the data into nice lines
    try:
        parse = x.split("INF:     ")  # Splits the segments into parts
        parse = parse[1]  # Takes 2nd index value and assigns it back to the
        full_string.append(parse)  # One line list and needs formatting
        #print("debug")
    except IndexError:
        pass
        full_string.append(x)  # One line list and needs formatting

print("Unparsed String: " + str(full_string))

full_string = [s.replace("20", "b") for s in full_string]  # Replace the 20's with 'b' for a symbolic 'blank'
full_string = [s.replace("1C", "_") for s in full_string]
full_string = [s.replace("1E", "_") for s in full_string]
full_string = [s.replace("\\n", "") for s in full_string]
full_string = [s.replace(" ", "") for s in full_string]
full_string = [s.replace("'", "") for s in full_string]
full_string = [s.replace("[", "") for s in full_string]
print(full_string)  # Debug line to check output at this point

formatted_string = ''.join(full_string)  # Rejoins the formatted strings in the list into one long string value - NEEDED
print("Formatted String: " + str(formatted_string))
print(type(formatted_string))
# formatted string *is* a string

### End of main program ###

### First Section of Map ###
company_ident(4)
term_class(1)
term_format_level(2)
multi_inq_flag(1)
resp_form_code(2)
req_form_code = req_form_code(2)  # This determines the Request Map
tran_type = tran_type(2)
seq_num(6)
date(6)
time(4)
term_loc_id(15)
comp_id(4)
uniq_dev_id(4)
### Track info ###
track_2()
#misc_data(11)  # Merged into new track_2 function logic

### Start of Request Type parsing output ###


if req_form_code == "D3" and tran_type == "01":
    print("Using " + req_form_code + " and " + tran_type)
    d3_01()
elif req_form_code == "D4" and tran_type == "01":
    print("Using " + req_form_code + " and " + tran_type)
    d4_01()
elif req_form_code == "C1" and tran_type == "01":
    print("Using " + req_form_code + " and " + tran_type)
    c1_01()
elif req_form_code == "C2" and tran_type == "01":
    print("Using " + req_form_code + " and " + tran_type)
    c2_01()
elif req_form_code == "B2" and tran_type == "05":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    b2_05()
elif req_form_code == "N0" and tran_type == "05":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    n0_05()
elif req_form_code == "P0" and tran_type == "05":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p0_05()
elif req_form_code == "P5" and tran_type == "05":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p5_05()
elif req_form_code == "P6" and tran_type == "05":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p6_05()
elif req_form_code == "P7" and tran_type == "05":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p7_05()
elif req_form_code == "P8" and tran_type == "05":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p8_05()
elif req_form_code == "B2" and tran_type == "11":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    b2_11()
elif req_form_code == "P0" and tran_type == "11":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p0_11()
elif req_form_code == "P5" and tran_type == "11":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p5_11()
elif req_form_code == "P6" and tran_type == "11":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p6_11()
elif req_form_code == "P7" and tran_type == "11":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p7_11()
elif req_form_code == "P8" and tran_type == "11":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p8_11()
elif req_form_code == "B2" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    b2_13()
elif req_form_code == "C1" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    c1_13()
elif req_form_code == "C2" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    c2_13()
elif req_form_code == "D3" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    d3_13()
elif req_form_code == "D4" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    d4_13()
elif req_form_code == "N0" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    n0_13()
elif req_form_code == "P0" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p0_13()
elif req_form_code == "P5" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p5_13()
elif req_form_code == "P6" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p6_13()
elif req_form_code == "P7" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p7_13()
elif req_form_code == "P8" and tran_type == "13":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p8_13()
elif req_form_code == "B2" and tran_type == "32":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    b2_32()
elif req_form_code == "C2" and tran_type == "32":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    c2_32()
elif req_form_code == "D4" and tran_type == "32":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    d4_32()
elif req_form_code == "N0" and tran_type == "32":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    n0_32()
elif req_form_code == "P3" and tran_type == "32":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p3_32()
elif req_form_code == "B2" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    b2_34()
elif req_form_code == "C2" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    c2_34()
elif req_form_code == "D3" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    d3_34()
elif req_form_code == "D4" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    d4_34()
elif req_form_code == "E3" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    e3_34()
elif req_form_code == "N0" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    n0_34()
elif req_form_code == "P0" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p0_34()
elif req_form_code == "P5" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p5_34()
elif req_form_code == "P6" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p6_34()
elif req_form_code == "P7" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p7_34()
elif req_form_code == "P8" and tran_type == "34":  # Has var data fields
    print("Using " + req_form_code + " and " + tran_type)
    p8_34()
else:
    print("Map not available")
