def solution(sizes):

    max_w = sizes[0][0]
    max_h = sizes[0][1]
    for w,h in sizes[1:]:

        temp_w = max(max_w,w)
        temp_h = max(max_h,h)

        temp_w2 = max(max_w,h)
        temp_h2 = max(max_h,w)

        if temp_w * temp_h > temp_w2 * temp_h2:
            max_w = temp_w2
            max_h = temp_h2
        else:
            max_w = temp_w
            max_h = temp_h
    return max_w * max_h


