# convert given BrainVis files to BIDS format and store those with matching filename

import csv

def convert_brainvision_to_bids(vmrk_file, bids_file):
  # Read the BrainVision VMRK file
  with open(vmrk_file, 'r') as f:
      lines = f.readlines()

  # Extract the marker information
  markers = []
  for line in lines:
      if line.startswith('Mk'):
          marker = line.split('=')[1].split(',')
          markers.append(marker)

  # Convert the marker information to BIDS format
  bids_markers = []
  for marker in markers:
      onset = float(marker[2]) / 500 # Convert from data points to seconds
      duration = float(marker[3]) / 500 # Convert from data points to seconds
      trial_type = marker[1]
      bids_markers.append({'onset': onset, 'duration': duration, 'trial_type': trial_type})

  # Write the BIDS markers to a text file
  with open(bids_file, 'w') as f:
      writer = csv.DictWriter(f, fieldnames=['onset', 'duration', 'trial_type'], delimiter='\t')
      writer.writeheader()
      writer.writerows(bids_markers)

  return bids_markers

# run the actual processing for all subjects
for subjectId in range(1, 51):

    # update paths and filenames
    path2subjectStr:str = f"./data/ds003702/sub-{subjectId:02d}/eeg/"
    filenameBrainvisionStr:str = f"sub-{subjectId:02d}_task-SocialMemoryCuing_eeg.vmrk"
    path2fileBvStr:str = path2subjectStr + filenameBrainvisionStr
    filenameBidsStr:str = f"sub-{subjectId:02d}_task-SocialMemoryCuing_events.tsv"
    path2fileBidsStr:str = path2subjectStr + filenameBidsStr

    # print the previously given files
    print(path2subjectStr)
    print(path2fileBvStr)
    print(path2fileBidsStr)

    try:
        # run the type conversion
        bids_markers = convert_brainvision_to_bids(
            vmrk_file = path2fileBvStr,
            bids_file = path2fileBidsStr
        )
    except:
        pass