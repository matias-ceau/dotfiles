-- Adds git related signs to the gutter, as well as utilities for managing changes
-- NOTE: gitsigns is already included in init.lua but contains only the base
-- config. This will add also the recommended keymaps.

return {
	{
		"lewis6991/gitsigns.nvim",
		opts = {
			signs = {
				add = { text = "+" },
				change = { text = "~" },
				delete = { text = "_" },
				topdelete = { text = "‾" },
				changedelete = { text = "~" },
			},
			on_attach = function(bufnr)
				local gitsigns = require("gitsigns")

				local function map(mode, l, r, opts)
					opts = opts or {}
					opts.buffer = bufnr
					vim.keymap.set(mode, l, r, opts)
				end

				-- Navigation
				map("n", "]c", function()
					if vim.wo.diff then
						vim.cmd.normal({ "]c", bang = true })
					else
						gitsigns.nav_hunk("next")
					end
				end, { desc = "Jump to next git [c]hange" })

				map("n", "[c", function()
					if vim.wo.diff then
						vim.cmd.normal({ "[c", bang = true })
					else
						gitsigns.nav_hunk("prev")
					end
				end, { desc = "Jump to previous git [c]hange" })

				-- Actions
				-- visual mode
				map("v", "<localleader>ghs", function()
					gitsigns.stage_hunk({ vim.fn.line("."), vim.fn.line("v") })
				end, { desc = "stage git hunk" })
				map("v", "<localleader>ghr", function()
					gitsigns.reset_hunk({ vim.fn.line("."), vim.fn.line("v") })
				end, { desc = "reset git hunk" })
				-- normal mode
				map("n", "<localleader>ghs", gitsigns.stage_hunk, { desc = "[g]it [s]tage hunk" })
				map("n", "<localleader>ghr", gitsigns.reset_hunk, { desc = "[g]it [r]eset hunk" })
				map("n", "<localleader>ghS", gitsigns.stage_buffer, { desc = "[g]it [S]tage buffer" })
				map("n", "<localleader>ghu", gitsigns.undo_stage_hunk, { desc = "[g]it [u]ndo stage hunk" })
				map("n", "<localleader>ghR", gitsigns.reset_buffer, { desc = "[g]it [R]eset buffer" })
				map("n", "<localleader>ghp", gitsigns.preview_hunk, { desc = "[g]it [p]review hunk" })
				map("n", "<localleader>ghb", gitsigns.blame_line, { desc = "[g]it [b]lame line" })
				map("n", "<localleader>ghd", gitsigns.diffthis, { desc = "[g]it [d]iff against index" })
				map("n", "<localleader>ghD", function()
					gitsigns.diffthis("@")
				end, { desc = "git [D]iff against last commit" })
				-- Toggles
				map(
					"n",
					"<localleader>gtb",
					gitsigns.toggle_current_line_blame,
					{ desc = "[g]it [t]oggle show [b]lame line" }
				)
				map("n", "<localleader>gtD", gitsigns.toggle_deleted, { desc = "[T]oggle git show [D]eleted" })
			end,
		},
	},
}
-- TODO: add explanation to which key
