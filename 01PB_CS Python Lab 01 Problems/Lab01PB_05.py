while(True):
    block_length = int(input("Enter block length: "))
    block_width = int(input("Enter block width: "))
    house_length = int(input("Enter house length: "))
    house_width = int(input("Enter house width: "))
    total_block = block_length*block_width
    total_house = house_length*house_width
    if (total_block < total_house) :
        print("invalid block value, block size must be equal or larger than house")
    else :
        # print(total_block,total_house)
        print(f"Mowing cost is {(total_block-total_house)*35} baht.")
        break
    

