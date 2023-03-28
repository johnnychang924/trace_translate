def Simple_to_ASCII(input_file_path, output_file_path, sector_size):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for i, row in enumerate(input_file):
            mode, s_LBA, offset = row.split()
            if mode == 'w' or mode == 'W':
                mode = 0
            else:
                mode = 1
            offset = int(int(offset) / sector_size)
            new_row = f"{i * 10} 0 {s_LBA} {offset} {mode}\n"
            output_file.write(new_row)

if __name__ == "__main__":
    input_file_path = "ssdTrace_399072.txt"
    output_file_path = "trace.txt"
    sector_size = 1

    Simple_to_ASCII(input_file_path, output_file_path, sector_size)
            