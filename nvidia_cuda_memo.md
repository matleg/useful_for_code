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

##

##
