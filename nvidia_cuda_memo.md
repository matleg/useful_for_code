## USE_CUDA

```bash
USE_CUDA=$(python -c "import torchvision, torch; print(torch.cuda.is_available())")
echo $USE_CUDA

```

## GPU use

```bash
watch -n -d 0.5 nvidia-smi

```

## Settings

```bash

/usr/bin/nvidia-settings

```

## Overheating ?

```bash
sudo systemctl restart nvidia-powerd.service
```

## cuda.is_available False

Try to disable secure boot

## CUDA & nvidia-smi

- Installer le BON driver sur windows:
La version du driver doit être <= à la version de nvidia-smi!

<https://www.nvidia.com/fr-fr/drivers/>

- dans docker:

erreur: `Failed to properly shut down NVML: GPU access blocked by the operating system`

mettre la variable `no-cgroups` à false dans:
`/etc/nvidia-container-runtime/config.toml`

- dans WSL:
  - bien regarder la compatibilité entre les versions runtime, nvcc (`nvcc --version`), system, etc.
<https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#id5>

  - le driver doit être installé sur windows, pas linux! <https://www.nvidia.com/en-us/drivers/> . Sur linux on installe le toolkit seulement!

- Liens utiles:  

  - > doc
<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/>

  - > explication:  
<https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi>

  - > compatibilité entre les versions:
<https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi>

la version de NVIDIA-SMI doit correspondre à celle du driver:

```txt
 ~ $ nvidia-smi.exe
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.76                 Driver Version: 560.76         CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
```

### test avec docker gpuburn

```sh
docker run --gpus all --rm oguzpastirmaci/gpu-burn 10
```

