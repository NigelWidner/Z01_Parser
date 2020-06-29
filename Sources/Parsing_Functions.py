def parse_cutter(string_cut):
    temp_string = ""
    global formatted_string  # Makes the full_string string avail. to the function
    for char in formatted_string[
                0:string_cut:1]:  # Loops through the specified range set by the value passed to the function
        temp_string = str(temp_string) + str(char)  # Creates the string snippet
        formatted_string = formatted_string.replace(char, "",
                                                    1)  # Cuts the original string after passing the needed value
    return temp_string
    return formatted_string

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

def track_2(length):
    track_2 = parse_cutter(length)
    print("track_2: " + track_2)


def misc_data(length):
    misc_data = parse_cutter(length)
    print("misc_data: " + misc_data)


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


def disc_data(length):
    disc_data = parse_cutter(length)
    print("disc_data: " + disc_data)


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


def POS_data_code(length):
    POS_data_code = parse_cutter(length)
    print("POS_data_code: " + POS_data_code)


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
    print("tag_data_length: " + tag_data_length)


def tag_data(length):
    tag_data = parse_cutter(length)
    print("tag_data: " + tag_data)


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
    print("pos_data_code: " + pos_data_code)


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


def avs_info(length):
    avs_info = parse_cutter(length)
    print("avs_info: " + avs_info)


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