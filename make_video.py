import cv2
import os
import argparse


def getTargetPath(directory_path, start_filename):
    filenames = os.listdir(directory_path)
    filenames.sort()
    filepaths = []
    for file in filenames:
        if file.startswith(start_filename):
            filepaths.append(os.path.join(args.directory_path, file))
    return filepaths

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process input filenames')
    parser.add_argument('-d', '--directory_path', type=str, default='/home/new/Pictures/',
                        help="full path to the images you want to merge")
    parser.add_argument('-s', '--start_filename', type=str, default='street',
                        help="starting string of file name")
    parser.add_argument("-o", "--output", type=str, default='test',
                        help="name for output video file")
    parser.add_argument("-fps", '--fps', type=float, default=30.0,
                        help="set fps for output video")
    parser.add_argument("-change_size", '--change_size', type=bool, default=False,
                        help="set size of output video")
    parser.add_argument("-width", '--output_width', type=int, default=640,
                        help="set width for output video")
    parser.add_argument("-height", '--output_height', type=int, default=480,
                        help="set height for output video")
    args = parser.parse_args()

    filepaths = getTargetPath(args.directory_path, args.start_filename)
    print(filepaths)

    output_directory = 'output'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    outputName = args.output + '.avi'
    output = os.path.join(output_directory, outputName)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = args.fps
    if args.change_size == False:
        image = cv2.imread(filepaths[0])
        height, width, _ = image.shape
        size = (width, height)
    else:
    	size = (args.output_width, args.output_height)
    print(size)
    # size = (args.output_width, args.output_height)
    videoWriter = cv2.VideoWriter(output, fourcc, fps, size)

    for file in filepaths:
        image = cv2.imread(file)
        if args.change_size == True:
        	image = cv2.resize(image, size)
        videoWriter.write(image)

    videoWriter.release()
