variable "map"{
  default = []
}

variable "image"{
  default = ""
}

variable "os_custom" {
	default = null
}

locals {

  map_values = [
    "/sjaskdask/daw",
    "/dslkjnasdnlk/kjasdk",
    "/hasnc/jas"
  ]

  map_keys = [
    "oracle7",
    "oracle8",
    "ubuntu"
  ]

  map = try(matchkeys(local.map_values,local.map_keys,[lower(var.os_custom)]))
  image = "bla/bla/bla${local.map[0]}"
}