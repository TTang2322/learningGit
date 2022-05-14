# non maximum suppression
# Input 
# bounding boxes: input_bboxes=[[x1, y1, x2, y2, score_1], ...]
# IoU threshold: iou_threshold
# output bboxes: Output_bboxes


def NMS(input_bboxes, iou_threshold):
    
    Output_bboxes = list()
    res = []
    
    for index_1, bboxes_item_1 in enumerate(input_bboxes):
        for index, bboxes_item_2 in enumerate(input_bboxes): #optimizition later, the bboxes_item_1 has been visited
            # if index <= index_1:
            #     continue
        
            in_h = min(bboxes_item_1[3], bboxes_item_2[3]) -max(bboxes_item_1[1],bboxes_item_2[1])
            in_w = min(bboxes_item_1[2],bboxes_item_2[2])- max(bboxes_item_1[0],bboxes_item_2[0])
        
            intersection_area = 0 if in_h <0 or in_w <0 else in_h * in_w
            unition_area = (bboxes_item_1[2] - bboxes_item_1[0])* (bboxes_item_1[3] - bboxes_item_1[1]) + \
                            (bboxes_item_2[2] - bboxes_item_2[0]) * (bboxes_item_2[3]-bboxes_item_2[1]) - intersection_area
            
            cur_iou = intersection_area / unition_area
            if cur_iou >= iou_threshold:
                if bboxes_item_1[4] >= bboxes_item_2[4]:
                    if bboxes_item_1 not in res:
                        res = bboxes_item_1
                else:
                    # continue
                    if bboxes_item_1 not in res:
                        res = bboxes_item_2
        # if index == len(input_bboxes)-index_1 and res is not None: 
        # Output_bboxes.append(res)
    
    return res
            
input_bboxes = [[1,1, 2,2, 0.6], [1,1, 2,2, 0.6], [1,1, 2,2, 0.6], [1,1, 2,2, 0.8]]
print("output:", NMS(input_bboxes, 0.5))

# caclulate cur_IOU for each two bboxes in input_bboxes

# decide whether the two bboxes should become only one 

