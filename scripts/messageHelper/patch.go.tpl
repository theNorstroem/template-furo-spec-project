package samplepb

// patch the target fields according to the update_mask
// this is not a very elegant implementation, but fast
func (target *Sample) PatchWithUpdateMask(delta *Sample) {
	for _, field := range delta.UpdateMask.Paths {
		switch field {

		case "tags":
			target.Tags = delta.Tags
		}

		if field == "display_name" {
			target.DisplayName = delta.DisplayName
		}

	}
}
