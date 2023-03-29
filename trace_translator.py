def Simple_to_ASCII(input_file_path, output_file_path, sector_size):
    write_sector_num = 0              # 總共寫入的sector數量(包含read before write)
    write_option_num = 0            # 總共的write trace數量
    read_sector_num = 0               # 總共讀取的sector數量
    read_option_num = 0             # 總共的read trace數量
    read_before_write_sector_num = 0  # 發生read before write的sector數量
    LSA_has_been_write = set()      # hash table
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for i, row in enumerate(input_file):
            mode, s_LSA, offset = row.split()
            offset = int(int(offset) / sector_size) # size in sector
            s_LSA = int(s_LSA)
            if mode == 'w' or mode == 'W':
                mode = 0
                write_option_num += 1
                write_sector_num += offset
                for j in range(offset):
                    LSA_has_been_write.add(s_LSA + j)
            else:
                mode = 1
                read_option_num += 1
                read_sector_num += offset
                for j in range(offset):
                    if s_LSA + j not in LSA_has_been_write:
                        write_sector_num += 1
                        read_before_write_sector_num += 1
            new_row = f"{i * 10} 0 {s_LSA} {offset} {mode}\n"
            output_file.write(new_row)
    return write_option_num, write_sector_num, read_option_num, read_sector_num, read_before_write_sector_num

def print_result(write_option_num, write_sector_num, read_option_num, read_sector_num, read_before_write_sector_num):
    print("Total write option num: ", write_option_num)
    print("Total read option num: ", read_option_num)
    print("Total write sector num(include read before write): ", write_sector_num)
    print("Total read sector num: ", read_sector_num)
    print("Total read before write sector num: ", read_before_write_sector_num)
    print("Percentage of read before write sector in total read sector num: ", read_before_write_sector_num / read_sector_num * 100, '%')

if __name__ == "__main__":
    #input_file_path = "trace\ssdTrace-02_extract.txt"
    #output_file_path = "ssdTrace_extract.txt"
    input_file_path = "trace\ssdTrace-399072.txt"
    output_file_path = "ssdTrace.txt"
    sector_size = 1

    result = Simple_to_ASCII(input_file_path, output_file_path, sector_size)
    print_result(*result)
    

            