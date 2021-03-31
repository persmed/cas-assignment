Artificial Intelligence
=======================

.. role:: bash(code)
   :language: bash

In this assignment you will run a deep learning-based algorithm with GPU to segment the proximal femur and the acetabulum from hip joint CT images. 

.. image:: img/HipJointCTSegmentation.png
   :scale: 40%
   :align: center




GPU by UBELIX
-------------
`UBELIX <https://ubelix.unibe.ch>`_ is an acronym and stands for University of Bern Linux Cluster, which is aimed for High Performance Computing (HPC). All staff and students of the University of Bern must have their Campus Account (CA) registered, before you can start working on the UBELIX. 

To request the `activation <https://hpc-unibe-ch.github.io/getting-Started/account.html>`_ of your Campus Account, please send an email to ``hpc@id.unibe.ch`` including a brief description of what you want to use the cluster for your Campus Account username. Students must additionally provide the name of the institute (e.g. Mathematical Institute) and the name of the research group (e.g. Numerical Analysis) if available. While the 'gpu' partition is not open for everybody automatically,  regular users must `request access to the GPU <https://hpc-unibe-ch.github.io/slurm/gpus.html>`_ partition explicitly before they can submit jobs running with GPU. You have to request access only once. To do so, simply write an email to ``hpc@id.unibe.ch`` and describe in a few words your application.  In this case, you can mention that you will  use deep learning for medical image analysis. 



File Transfer to/from UBELIX
----------------------------
At some point, you will probably need to copy files between your local computer and the cluster. There are different ways to achieve this, depending on your local operating system (OS). To copy a file from your local computer running a UNIX-like OS use the secure copy command scp on your local workstation:

.. code-block:: bash

    scp /path/to/file <username>@submit.unibe.ch:/path/to/target_dir/

To copy a file from the cluster to your local computer running a UNIX-like OS also use the secure copy command scp on your local workstation:

.. code-block:: bash

	scp <username>@submit.unibe.ch:/path/to/file /path/to/target_dir/
    
More information about file transfer can be found at `File Transfer <https://hpc-unibe-ch.github.io/file-system/file-transfer.html>`_

Code Explanation 
----------------
The package file :bash:`hip_ct_unet_CAS_code.zip` includes the code and data for hip joint CT segmentation based on U-Net.  As the package is quite large, so we put it on ilias instead of on github. Your task is to train it on UBELIX and report your running results. 

#. Image Dataset
	- :bash:`data_loader.py` functions as data provider for training 
	- The :bash:`dataset` folder contains all of the training and validation images in 2D format, which are extracted from 3D volume CT images
	- 10 3D CT hip images were used for training, and each of them consists of roughly 240 slices. Therefore, we have in total around 2400 slice images for training. 
	  

#. U-Net Implementation 
	- :bash:`model.py` implements the U-Net, whichi is a fully convolutional neural network that was developed for biomedical image segmentation.
	- The network consists of a contracting path and an expansive path, which gives it the u-shaped architecture. The contracting path is a typical convolutional network that consists of repeated application of convolutions, each followed by a rectified linear unit (ReLU) and a max pooling operation. During the contraction, the spatial information is reduced while feature information is increased. The expansive pathway combines the feature and spatial information through a sequence of up-convolutions and concatenations with high-resolution features from the contracting path.
	
#. Model Training 
	- The training will be conducted in :bash:`train.py`. All models after each epoch training will saved under the foder :bash:`./checkpoint`.
	- By default, the batch size is 8, so there are 2400/8=300 iterations in each epoch. And the default number of training epochs is 10, so the model will be trained by 3000 iterations in default. After the training, you can find the training loss at :bash:`./log/training_loss.png`.
	  
#. Test on Unseen data 
	- A new and unseen hip CT image for testing is prepared at :bash:`./Test/21_data.nii.gz`.
	- :bash:`python test.py` will do the automatic segmentation for the test data, and the prediction will be saved under the same foder at :bash:`./Test/21_pred_segmentation.nii.gz`. 
	- The segmentation nifti file will be post-processed by removing isolated regions and saved at :bash:`./Test/21_post_segmentation.nii.gz`.
	  
#. Evaluation
	- :bash:`evaluate.py` will comapre the automatic segmentation result :bash:`./Test/21_post_segmentation.nii.gz` with the ground truth manual segmentation :bash:`./Test/21_mask.nii.gz`. The results of Dice, ASD, and HD will be saved at './Test/results.txt'.



Training U-Net for Semantic Segmentation
----------------------------------------

.. image:: img/ITKSNAP.png
   :scale: 30%
   :align: center

#. Install 'ITK-SNAP' and view the CT data and segmentation 
	- Install `ITK-SNAP <http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP3>`_  
	- unzip the file 'hip_ct_unet_CAS_code.zip' on your local machine. 
	- Inside the unzipped folder, you can find a test hip CT image and its segmentation ground truth at ``Test/21_data.nii.gz`` and ``Test/21_mask.nii.gz``, respectively. 
	- Drag the data file into ITK-SNAP and then load the mask data as segmentation, the visualization should be like the figure above

#. Change to your own email
	- Change <username>@students.unibe.ch to your email in the file of 'job_run_gpu.sh' under the unzipped folder
	- delete the original 'hip_ct_unet_CAS_code.zip'
	- zip the folder 'hip_ct_unet_CAS_code' to 'hip_ct_unet_CAS_code.zip'

#. Upload the project to UBELIX
	- :bash:`scp /path/to/hip_ct_unet_CAS_code.zip <username>@submit.unibe.ch:~/`
	
#. Login and Unzip the Code
	- :bash:`ssh <username>@submit.unibe.ch`
	- :bash:`cd ~`
	- :bash:`ls`
	- :bash:`unzip hip_ct_unet_CAS_code.zip`
	
#. Submit the job running application
	- :bash:`cd hip_ct_unet_CAS_code`
	- :bash:`sbatch job_run_gpu.sh`
	- In the first time running, UBELIX will build the docker container and it may take up to 10 minutes
	
#. Check the logging
    - All loggings will be stored at slurm-xxxxxxxx.out in current folder
    - The file of slurm-xxxxxxxx.out can be found at by the command of :bash:`ls`
    - Check the logging by :bash:`cat slurm-<xxxxxxxx>.out`

#. Check the segmentation results
    - The training with GPU will take around 30 minutes
    - Copy the training loss figure to local machine : :bash:`scp <username>@submit.unibe.ch:~/hip_ct_unet_CAS_code/log/training_loss.png` :bash:`/path/to/training_loss.png`
    - Copy the segmentation results in nifti file to local machine  and then show it in ITK-SNAP: :bash:`scp <username>@submit.unibe.ch:~/hip_ct_unet_CAS_code/Test/21_pred_segmentation.nii.gz` :bash:`/path/to/21_pred_segmentation.nii.gz`
    - Copy the evaluation results includes Dice, ASD, HD to local machine: :bash:`scp <username>@submit.unibe.ch:~/hip_ct_unet_CAS_code/Test/results.txt` :bash:`/path/to/Test/results.txt`


Report
------
Run the code of deep learning for hip ct image segmentation, and write a short report  where to address the following questions. 

#. Experiment Running (5 points)
	- Show the 3D models of automatic segmentation and ground truth segmentation in individual ITK-SNAP applications, and then compare them qualitatively.  (2 points)
	- Show the training loss curve (1 point)
	- What is your evaluation result of Dice, ASD, and HD ?  Do a screenshot of the result text file.  (1 point)
	- Do a screenshot of the training logging file, which is slurm-xxxxxxxx.out mentioned before. (1 point)

#. Questions (5 points)
	- What is semantic segmentation in a hip CT image? (1 point)
	- How could the segmentation of the hip joint be used in clinical practice? (1 point)
	- What is training / validation / test dataset ? (1 point)
	- Explain the U-net architecture, like how many conv layers, pooling layers. Why is it better than a fully connected network for segmentation? (1 point)
	- Which hyper parameters are important during the network training? Why? (1 point)
 


Submission
----------
Upload the report file in PDF with filename ``lastname_firstname_assignment2_AI_report.pdf``




Materials
---------
* https://ubelix.unibe.ch
* https://hpc-unibe-ch.github.io/quick-start.html

